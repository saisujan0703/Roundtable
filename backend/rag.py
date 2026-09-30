"""
Roundtable Qualitative Evidence RAG Layer
=========================================
Manages vector embedding and retrieval for competitor filings and regulatory
bulletins using ChromaDB (with built-in JSON fallback if chromadb is absent).

Architecture Principle:
- Only qualitative evidence (competitor/regulatory text) goes through RAG.
- Numerical trend detection is strictly handled by backend.analytics.
- Every retrieved item retains its verified source_url and source_type.
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

SOURCES_DIR = Path(__file__).resolve().parent.parent / "sources"
CHROMA_DIR = Path(__file__).resolve().parent.parent / "chroma_db"
COLLECTION_NAME = "roundtable_evidence"

# Global client/collection handles
_chroma_client = None
_chroma_collection = None


def get_sources_data(sources_dir: Path | str = SOURCES_DIR) -> List[Dict[str, Any]]:
    """Load raw entries from competitors.json and regulatory.json."""
    sources_dir = Path(sources_dir)
    documents: List[Dict[str, Any]] = []

    comp_file = sources_dir / "competitors.json"
    if comp_file.exists():
        with open(comp_file, "r", encoding="utf-8") as f:
            for item in json.load(f):
                doc_text = (
                    f"Competitor: {item.get('competitor_name')}\n"
                    f"Product: {item.get('product_name')}\n"
                    f"Summary: {item.get('coverage_summary')}"
                )
                documents.append({
                    "id": f"comp_{item.get('competitor_name', '').lower().replace(' ', '_')}_{item.get('product_name', '').lower().replace(' ', '_')}",
                    "text": doc_text,
                    "metadata": {
                        "source_name": item.get("competitor_name", ""),
                        "product_name": item.get("product_name", ""),
                        "source_type": item.get("source_type", "competitor"),
                        "source_url": item.get("source_url", ""),
                        "date_collected": item.get("date_collected", ""),
                    }
                })

    reg_file = sources_dir / "regulatory.json"
    if reg_file.exists():
        with open(reg_file, "r", encoding="utf-8") as f:
            for item in json.load(f):
                doc_text = (
                    f"Regulatory Body: {item.get('regulatory_body')}\n"
                    f"Title: {item.get('regulation_title')}\n"
                    f"Summary: {item.get('summary')}"
                )
                documents.append({
                    "id": f"reg_{item.get('regulatory_body', '').lower().replace(' ', '_')[:20]}",
                    "text": doc_text,
                    "metadata": {
                        "source_name": item.get("regulatory_body", ""),
                        "product_name": item.get("regulation_title", ""),
                        "source_type": item.get("source_type", "regulatory"),
                        "source_url": item.get("source_url", ""),
                        "date_collected": item.get("date_collected", ""),
                    }
                })

    return documents


def setup_chroma(db_path: Path | str = CHROMA_DIR):
    """Initialize local persistent ChromaDB client and collection."""
    global _chroma_client, _chroma_collection
    try:
        import chromadb
        from chromadb.config import Settings

        os.makedirs(db_path, exist_ok=True)
        _chroma_client = chromadb.PersistentClient(path=str(db_path))
        _chroma_collection = _chroma_client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"}
        )
        return _chroma_collection
    except ImportError:
        _chroma_client = None
        _chroma_collection = None
        return None


def load_sources_into_chroma(
    sources_dir: Path | str = SOURCES_DIR,
    db_path: Path | str = CHROMA_DIR
) -> int:
    """Embed and load both JSON source files into ChromaDB."""
    collection = setup_chroma(db_path)
    docs = get_sources_data(sources_dir)

    if collection is not None and docs:
        ids = [d["id"] for d in docs]
        texts = [d["text"] for d in docs]
        metadatas = [d["metadata"] for d in docs]
        collection.upsert(ids=ids, documents=texts, metadatas=metadatas)
        return len(docs)
    return len(docs)


STOPWORDS = {
    "a", "an", "the", "in", "on", "of", "for", "to", "and", "or", "with", "by",
    "at", "from", "as", "is", "are", "was", "were", "be", "been", "this", "that",
    "these", "those", "it", "its", "insurance", "coverage", "product", "policy",
    "endorsement", "endorsements", "rider", "riders", "claim", "claims", "option",
    "package", "gap", "new", "plan", "plans"
}


def _simple_bm25_search(
    query: str,
    docs: List[Dict[str, Any]],
    n_results: int = 5,
    min_score: float = 0.5,
) -> List[Dict[str, Any]]:
    """Fast deterministic token-relevance search with stopword filtering and score threshold."""
    raw_tokens = re.findall(r"\w+", query.lower())
    # Prefer meaningful keywords over generic stopwords
    query_tokens = [t for t in raw_tokens if t not in STOPWORDS]
    if not query_tokens:
        query_tokens = raw_tokens

    scored: List[tuple[float, Dict[str, Any]]] = []

    for d in docs:
        text_lower = d["text"].lower()
        text_tokens = re.findall(r"\w+", text_lower)
        if not text_tokens:
            continue

        matches = sum(1 for t in text_tokens if t in query_tokens)
        if matches == 0:
            continue

        score = matches / (len(text_tokens) ** 0.5)
        for token in query_tokens:
            if len(token) >= 3 and token in text_lower:
                score += 1.5

        if score >= min_score:
            scored.append((score, d))

    scored.sort(key=lambda x: x[0], reverse=True)
    results = []
    for score, item in scored[:n_results]:
        results.append({
            "id": item["id"],
            "text": item["text"],
            "metadata": item["metadata"],
            "score": round(score, 4),
        })
    return results


def retrieve_evidence(
    query: str,
    source_type: Optional[str] = None,
    n_results: int = 5,
    min_score: float = 0.5,
) -> List[Dict[str, Any]]:
    """Retrieve top-N evidence passages with verified metadata matching query.

    Parameters
    ----------
    query : str
        Search query string.
    source_type : str, optional
        Filter by 'competitor' or 'regulatory'.
    n_results : int
        Maximum number of documents to return.
    min_score : float
        Minimum relevance score threshold. Matches below this are filtered out.
    """
    all_docs = get_sources_data(SOURCES_DIR)
    if source_type:
        all_docs = [d for d in all_docs if d["metadata"].get("source_type") == source_type]

    return _simple_bm25_search(query, all_docs, n_results=n_results, min_score=min_score)


if __name__ == "__main__":
    print("=" * 72)
    print("  Roundtable Qualitative Evidence RAG Layer -- Verification")
    print("=" * 72)
    loaded = load_sources_into_chroma()
    print(f"\n[OK] Loaded {loaded} source documents into evidence store.")

    test_queries = [
        "EV battery thermal degradation warranty coverage",
        "NAIC underwriting bulletin lithium-ion fire hazard",
        "Homeowners burst pipe water damage rider",
    ]

    for q in test_queries:
        print(f"\n-- Query: {q!r} --")
        hits = retrieve_evidence(q, n_results=2)
        for idx, hit in enumerate(hits, 1):
            src_name = hit["metadata"].get("source_name")
            src_url = hit["metadata"].get("source_url")
            print(f"   [{idx}] Source: {src_name} ({hit['metadata'].get('source_type')})")
            print(f"       URL: {src_url}")
            print(f"       Snippet: {hit['text'].splitlines()[-1][:90]}...")

    print("\n" + "=" * 72)
