"""
Authentication and role-based access for the Roundtable API.

Users sign in with email + password + the role they are signing in as. Passwords are stored as
salted PBKDF2-SHA256 hashes; a successful sign-in returns an opaque bearer token backed by the
`auth_sessions` table (so sign-out and expiry are enforced server side). Repeated wrong passwords
lock the account for a few minutes.

Roles:
- Claims Lead  -> Claims workspace: reviews and edits claims artifacts, signs non-actuarial gates
- Lead Actuary -> Actuarial workspace: actuarial recommendation and actuarial launch sign-off
Reading is open to any signed-in user; `required_role()` decides who may write.
"""
from __future__ import annotations

import hashlib
import hmac
import os
import re
import secrets
from datetime import datetime, timedelta
from typing import Optional

from backend.database import get_connection

CLAIMS_LEAD = "Claims Lead"
LEAD_ACTUARY = "Lead Actuary"
ROLES = (CLAIMS_LEAD, LEAD_ACTUARY)

SESSION_HOURS = 8
MAX_FAILED_ATTEMPTS = 5
LOCKOUT_MINUTES = 10
_PBKDF2_ITERATIONS = 200_000

# Seed accounts, created once if missing. Override the passwords with these env vars before first start.
SEED_USERS = (
    ("claims.lead@carrier.com", "Claims Lead", CLAIMS_LEAD, "ROUNDTABLE_CLAIMS_PASSWORD", "Claims@2026"),
    ("lead.actuary@carrier.com", "Lead Actuary", LEAD_ACTUARY, "ROUNDTABLE_ACTUARY_PASSWORD", "Actuary@2026"),
)


def _now() -> datetime:
    return datetime.utcnow()


def hash_password(password: str, salt: Optional[bytes] = None) -> str:
    salt = salt or secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, _PBKDF2_ITERATIONS)
    return f"pbkdf2_sha256${_PBKDF2_ITERATIONS}${salt.hex()}${digest.hex()}"


def verify_password(password: str, stored: str) -> bool:
    try:
        _, iterations, salt_hex, digest_hex = stored.split("$")
        digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), bytes.fromhex(salt_hex), int(iterations))
    except (ValueError, TypeError):
        return False
    return hmac.compare_digest(digest.hex(), digest_hex)


def init_auth_tables() -> None:
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                email TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                role TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                failed_attempts INTEGER NOT NULL DEFAULT 0,
                locked_until TEXT,
                created_at TEXT NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS auth_sessions (
                token_hash TEXT PRIMARY KEY,
                email TEXT NOT NULL REFERENCES users(email),
                created_at TEXT NOT NULL,
                expires_at TEXT NOT NULL
            )
        """)
        for email, name, role, env_var, default_password in SEED_USERS:
            if conn.execute("SELECT 1 FROM users WHERE email = ?", (email,)).fetchone() is None:
                conn.execute(
                    "INSERT INTO users (email, name, role, password_hash, created_at) VALUES (?, ?, ?, ?, ?)",
                    (email, name, role, hash_password(os.getenv(env_var, default_password)), _now().isoformat()),
                )
        conn.execute("DELETE FROM auth_sessions WHERE expires_at < ?", (_now().isoformat(),))


def _token_hash(token: str) -> str:
    # Only a hash of the token is stored, so a leaked database can't be replayed as live sessions
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


class AuthError(Exception):
    def __init__(self, status: int, detail: str):
        super().__init__(detail)
        self.status = status
        self.detail = detail


def login(email: str, password: str, role: str) -> dict:
    """Check the credentials and that the account holds `role`; return a new session."""
    email = (email or "").strip().lower()
    invalid = AuthError(401, "Invalid email or password.")
    with get_connection() as conn:
        user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        if user is None:
            verify_password(password, hash_password("timing-equaliser"))
            raise invalid
        if user["locked_until"] and datetime.fromisoformat(user["locked_until"]) > _now():
            raise AuthError(423, f"Account locked after {MAX_FAILED_ATTEMPTS} failed sign-ins. "
                                 f"Try again in {LOCKOUT_MINUTES} minutes.")
        if not verify_password(password or "", user["password_hash"]):
            attempts = user["failed_attempts"] + 1
            locked = (_now() + timedelta(minutes=LOCKOUT_MINUTES)).isoformat() if attempts >= MAX_FAILED_ATTEMPTS else None
            conn.execute("UPDATE users SET failed_attempts = ?, locked_until = ? WHERE email = ?",
                         (0 if locked else attempts, locked, email))
            raise invalid
        if user["role"] != role:
            raise AuthError(403, f"This account is not authorised for the {role} workspace.")
        conn.execute("UPDATE users SET failed_attempts = 0, locked_until = NULL WHERE email = ?", (email,))
        token = secrets.token_urlsafe(32)
        expires = _now() + timedelta(hours=SESSION_HOURS)
        conn.execute("INSERT INTO auth_sessions (token_hash, email, created_at, expires_at) VALUES (?, ?, ?, ?)",
                     (_token_hash(token), email, _now().isoformat(), expires.isoformat()))
    return {"token": token, "expires_at": expires.isoformat() + "Z",
            "user": {"email": user["email"], "name": user["name"], "role": user["role"]}}


def user_for_token(token: str) -> Optional[dict]:
    with get_connection() as conn:
        row = conn.execute("""
            SELECT u.email, u.name, u.role FROM auth_sessions s JOIN users u ON u.email = s.email
            WHERE s.token_hash = ? AND s.expires_at > ?
        """, (_token_hash(token), _now().isoformat())).fetchone()
    return dict(row) if row else None


def logout(token: str) -> None:
    with get_connection() as conn:
        conn.execute("DELETE FROM auth_sessions WHERE token_hash = ?", (_token_hash(token),))


# ---------------------------------------------------------------------------
# Access policy: which role may call a write endpoint (None = any signed-in user)
# ---------------------------------------------------------------------------
_BRIEF_PATH = re.compile(r"^/api/briefs/\d+/(?P<rest>.+)$")


def required_role(method: str, path: str) -> Optional[str]:
    if method in ("GET", "HEAD", "OPTIONS"):
        return None
    m = _BRIEF_PATH.match(path)
    if not m:
        return None  # creating briefs, idea assistant, voice input: any signed-in role
    rest = m.group("rest")
    if rest == "proxies" or rest == "workflow/decision":
        return None
    if rest.startswith("workflow/review/"):
        return LEAD_ACTUARY if rest.endswith("/actuarial") else CLAIMS_LEAD
    if rest.startswith("launch-gate/"):
        return LEAD_ACTUARY if rest == "launch-gate/actuarial" else CLAIMS_LEAD
    # Claims findings, notes, readiness, guideline, scenarios, letters, compliance, policy form, coverage
    return CLAIMS_LEAD
