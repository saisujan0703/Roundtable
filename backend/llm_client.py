"""
Roundtable LLM Client
=====================
One structured-output call used by every LLM feature (brief synthesis, idea assistant, guideline,
test scenarios, letters), with two interchangeable providers:

- anthropic : Claude via the Anthropic SDK (ANTHROPIC_API_KEY, model ANTHROPIC_MODEL)
- gemini    : Google Gemini via the google-genai SDK (GEMINI_API_KEY, model GEMINI_MODEL) — has a free tier

LLM_PROVIDER picks one explicitly ("anthropic", "gemini" or "none"). If unset, the first provider with a
key and an installed SDK is used, Claude first. With none available, callers get LLMUnavailable and use
their rule-based fallback, exactly as before.

Every call returns a dict matching the caller's JSON schema; server-side validation stays in the callers.
"""
from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

DEFAULT_ANTHROPIC_MODEL = "claude-sonnet-5"
DEFAULT_GEMINI_MODEL = "gemini-3.8-flash"  # gemini-2.5-flash is closed to new users
# Tried in order when the main model is busy, out of free-tier quota (20 requests/day per model) or retired;
# each model has its own quota. Override with GEMINI_FALLBACK_MODELS="model-a,model-b" ("" disables).
DEFAULT_GEMINI_FALLBACKS = "gemini-3.5-flash,gemini-3.1-flash-lite"
_GEMINI_SWITCH_CODES = (404, 429, 500, 503)

# generation_method values stored on briefs, guidelines, scenarios and letters
METHOD = {"anthropic": "anthropic_claude", "gemini": "google_gemini"}


class LLMUnavailable(RuntimeError):
    """No provider configured (no key, SDK missing, or LLM_PROVIDER=none)."""


def _has_module(name: str) -> bool:
    try:
        __import__(name)
        return True
    except ImportError:
        return False


def _gemini_key() -> Optional[str]:
    return os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")


def provider() -> Optional[str]:
    """The active provider name, or None when no LLM can be used."""
    available = {
        "anthropic": bool(os.environ.get("ANTHROPIC_API_KEY")) and _has_module("anthropic"),
        "gemini": bool(_gemini_key()) and _has_module("google.genai"),
    }
    chosen = (os.environ.get("LLM_PROVIDER") or "").strip().lower()
    if chosen == "none":
        return None
    if chosen in available:
        return chosen if available[chosen] else None
    return next((p for p in ("anthropic", "gemini") if available[p]), None)


def method_name() -> Optional[str]:
    """generation_method for output written by the active provider (None when there is none)."""
    p = provider()
    return METHOD[p] if p else None


def structured_call(system: str, messages: List[Dict[str, str]], name: str, description: str,
                    schema: Dict[str, Any], max_tokens: int = 8000) -> Dict[str, Any]:
    """Ask the active provider for one JSON object matching *schema*.

    *messages* is a chat history of {"role": "user" | "assistant", "content": str}, starting and ending
    with a user turn. Raises LLMUnavailable when no provider is configured, RuntimeError on a bad reply,
    or the SDK's own exception on API failures; callers treat all of these as "use the fallback".
    """
    p = provider()
    if p == "anthropic":
        return _anthropic(system, messages, name, description, schema, max_tokens)
    if p == "gemini":
        return _gemini(system, messages, name, description, schema, max_tokens)
    raise LLMUnavailable("No LLM provider configured (set ANTHROPIC_API_KEY or GEMINI_API_KEY).")


# ---------------------------------------------------------------------------
# Claude
# ---------------------------------------------------------------------------
def _anthropic(system, messages, name, description, schema, max_tokens) -> Dict[str, Any]:
    import anthropic

    client = anthropic.Anthropic()
    model = os.environ.get("ANTHROPIC_MODEL", DEFAULT_ANTHROPIC_MODEL)
    tool = {"name": name, "description": description, "input_schema": schema}
    request = dict(model=model, max_tokens=max_tokens, system=system, messages=messages, tools=[tool])
    try:
        response = client.messages.create(**request, tool_choice={"type": "tool", "name": name})
    except anthropic.BadRequestError as e:
        # Newer models (e.g. Claude Opus 5.5, Sonnet 5.5) reject forced tool use: let the model call the
        # tool itself, with an explicit instruction to do so
        if "tool_choice" not in str(e):
            raise
        request["system"] = f"{system}\n\nRespond only by calling the {name} tool."
        response = client.messages.create(**request, tool_choice={"type": "auto"})
    if response.stop_reason == "refusal":
        raise RuntimeError("Claude declined the request.")
    for block in response.content:
        if block.type == "tool_use" and block.name == name:
            return dict(block.input)
    raise RuntimeError(f"Claude did not call {name} (stop_reason={response.stop_reason}).")


# ---------------------------------------------------------------------------
# Gemini
# ---------------------------------------------------------------------------
# JSON Schema keywords Gemini's response_json_schema accepts (see google-genai GenerateContentConfig)
_GEMINI_KEYS = {"$id", "$defs", "$ref", "$anchor", "type", "format", "title", "description", "enum", "items",
                "prefixItems", "minItems", "maxItems", "minimum", "maximum", "anyOf", "oneOf", "properties",
                "additionalProperties", "required", "propertyOrdering"}


def gemini_schema(node: Any) -> Any:
    """Drop JSON Schema keywords Gemini rejects (maxLength, default, ...); a $ref node keeps only $-keys."""
    if isinstance(node, list):
        return [gemini_schema(n) for n in node]
    if not isinstance(node, dict):
        return node
    if "$ref" in node:
        return {k: v for k, v in node.items() if k.startswith("$")}
    # Gemini rejects item-count limits on arrays of objects as too complex (400 INVALID_ARGUMENT);
    # callers enforce those caps server-side anyway
    object_items = isinstance(node.get("items"), dict) and (node["items"].get("type") == "object" or "$ref" in node["items"])
    out = {}
    for k, v in node.items():
        if k not in _GEMINI_KEYS or (object_items and k in ("minItems", "maxItems")):
            continue
        if k in ("properties", "$defs"):
            out[k] = {name: gemini_schema(sub) for name, sub in v.items()}
        elif k == "enum":
            out[k] = v
        else:
            out[k] = gemini_schema(v)
    return out


def _gemini(system, messages, name, description, schema, max_tokens) -> Dict[str, Any]:
    from google import genai
    from google.genai import types

    from google.genai import errors

    # Free-tier models often return 503 "high demand" for a few seconds: retry briefly, then try the next model
    client = genai.Client(api_key=_gemini_key(), http_options=types.HttpOptions(
        retry_options=types.HttpRetryOptions(attempts=3, initial_delay=2.0, max_delay=10.0, http_status_codes=[500, 503])))
    fallbacks = os.environ.get("GEMINI_FALLBACK_MODELS", DEFAULT_GEMINI_FALLBACKS)
    models = [os.environ.get("GEMINI_MODEL", DEFAULT_GEMINI_MODEL)] + [m.strip() for m in fallbacks.split(",") if m.strip()]
    contents = [types.Content(role="model" if m["role"] == "assistant" else "user", parts=[types.Part(text=m["content"])])
                for m in messages]
    config = types.GenerateContentConfig(
        system_instruction=(f"{system}\n\nRespond with a single JSON object for '{name}' ({description}) that "
                            "matches the response schema exactly."),
        response_mime_type="application/json",
        response_json_schema=gemini_schema(schema),
        # Gemini counts its thinking tokens against this limit, so leave room beyond the answer itself
        max_output_tokens=min(max_tokens * 2, 60000),
    )
    for n, model in enumerate(models):
        try:
            response = client.models.generate_content(model=model, contents=contents, config=config)
            break
        except errors.APIError as e:
            if e.code not in _GEMINI_SWITCH_CODES or n == len(models) - 1:
                raise
            print(f"[NOTE: Gemini] {model} unavailable ({e.code}); trying {models[n + 1]}")
    text = response.text
    if not text:
        reason = response.candidates[0].finish_reason if response.candidates else "no candidates"
        raise RuntimeError(f"Gemini returned no content (finish_reason={reason}).")
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Gemini returned invalid JSON: {e}") from e
    if not isinstance(data, dict):
        raise RuntimeError("Gemini returned JSON that is not an object.")
    return data
