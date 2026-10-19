# Roundtable

Roundtable is decision support for launching a new insurance product. It turns claims data, competitor intelligence and regulatory sources into cited product briefs, actuarial pricing and launch-readiness work for Claims and Actuarial teams on Guidewire PolicyCenter and ClaimCenter.

A product manager describes an idea ("EV owners keep getting denied for battery damage"). Roundtable finds the claims behind it, checks what competitors and regulators say, and gives each team the work it must finish before go-live, ending in a go/no-go launch gate.

> **Demo data.** The claims, policies and exposures in `roundtable.db` are synthetic. Every number and recommendation is directional and needs review by a qualified actuary or claims professional before real use.

## What it does

**Product decision brief**
- Matches the idea to a risk pattern in the claims data. When the product has no history of its own, it uses related patterns as proxies.
- Analyses frequency, severity, trend, loss ratio, coverage-gap denials, reserve development and claim handling, all computed in Python and SQL.
- Pulls competitor and regulatory evidence from a curated library and live web research. Every qualitative statement must cite a retrieved source.
- Verifies model-written text after generation: numbers, citations, trend wording and named carriers or regulators.
- Flags conflicting evidence. One example: the claims data looks favourable while competitors withdrew similar cover after losses.

**Actuarial workspace**
- Rate indication: CAT and large-loss treatment, chain-ladder and Bornhuetter-Ferguson development, trend, behavioural loads, credibility with external benchmarks, and expense, ULAE and profit provisions.
- Company assumptions with cited sources. Profit and contingencies are derived from the target return on equity.
- Rating plan: Poisson GLM frequency relativities, deductible and increased-limit factors, balanced to the indicated premium.
- Parametric pricing, a 3-year business plan with stress tests, and actual-vs-expected monitoring.
- Draft actuarial memorandum with exhibits and ASOP references, plus PolicyCenter rating-engine test cases.
- Approval of the selected rate. The approval goes stale when the inputs change.

**Claims workspace**
- Covered-claims set: which historical claims the new coverage would pay.
- Readiness checklist, claims handling guideline, ClaimCenter test scenarios and customer letter templates.
- Launch operations plan (staffing, large-loss thresholds, statutory lines, Medicare Section 111, litigation) and a state claims-compliance matrix.
- Policy-form upload with an exclusion screen against the claims data.

**Across the platform**
- Go/no-go launch gate with sign-offs from Claims, Claims Legal, Compliance, Product, Actuarial and Finance.
- Market Radar: news watch that proposes product opportunities, backed by claims evidence.
- Library: custom keyword risk patterns and user-added competitor and regulatory sources, with reviewed web search.
- Sign-in with roles, account lockout, and an append-only audit log of every change.
- Idea assistant with voice input (local speech-to-text).

## Architecture

```
Streamlit UI (frontend/)  ──HTTP──▶  FastAPI (backend/main.py)
                                        ├─ analytics, pricing, reserving, rating_plan, business_plan ...  (pandas / NumPy)
                                        ├─ llm, llm_client  (Claude or Gemini; writes text, never numbers)
                                        ├─ rag, evidence_sources  (curated + user-added sources)
                                        ├─ verification, conflicts  (deterministic checks on model output)
                                        └─ roundtable.db  (SQLite: claims, policies, exposures, briefs, audit log)
```

## Tech stack

Python, FastAPI, Streamlit, SQLite, pandas, NumPy, Pydantic, Anthropic Claude and Google Gemini APIs, Tavily web search, faster-whisper, pypdf, pytest.

## Getting started

Requires Python 3.10 or later.

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root. Everything is optional; without an LLM key, Roundtable uses rule-based fallbacks.

```env
# LLM: Claude, or Gemini's free tier. LLM_PROVIDER = anthropic | gemini | none (default: first key found)
ANTHROPIC_API_KEY=
GEMINI_API_KEY=
LLM_PROVIDER=

# Live web research, Market Radar news and source search
TAVILY_API_KEY=

# Passwords for the two seed accounts (set before the first start)
ROUNDTABLE_CLAIMS_PASSWORD=
ROUNDTABLE_ACTUARY_PASSWORD=
```

Run the backend and the frontend in two terminals:

```bash
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
python -m streamlit run frontend/app.py
```

Open http://localhost:8501. API docs are at http://127.0.0.1:8000/docs.

Two accounts are created on first start:

| Role | Email | Default password |
|---|---|---|
| Claims Lead | `claims.lead@carrier.com` | `Claims@2026` |
| Lead Actuary | `lead.actuary@carrier.com` | `Actuary@2026` |

Change the defaults with the environment variables above before exposing Roundtable to anyone else.

To rebuild the synthetic database, run `python data/generate_data.py`.

## Tests

```bash
pip install -r requirements-dev.txt
python -m pytest
```

The suite checks the pricing, reserving and business-plan maths against hand calculations and runs end-to-end API tests on a temporary copy of `roundtable.db`, so the real database is never changed.

## Project structure

```
backend/     FastAPI app and all analytics, pricing, LLM, verification and workflow modules
frontend/    Streamlit app (app.py) and one panel module per section
data/        Synthetic data generator
sources/     Curated competitor, regulatory and state claims-rule sources
docs/        Guidewire reference: entity data dictionaries, typelist catalogs, guides
tests/       pytest suite
```

## Limitations

- Synthetic data. Development triangles are reconstructed because the data has no payment or reserve-change history.
- No live Guidewire integration. The PolicyCenter and ClaimCenter data model is used as reference only.
- SQLite and a single server: suited to demos and pilots, not production.
- State claims rules are loaded for 9 states; the rest fall back to the NAIC model and are flagged.
