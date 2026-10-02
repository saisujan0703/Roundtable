"""
Roundtable Data Models
======================
Pydantic schemas for the Product Decision Brief generation pipeline.

Enforces core architecture rules:
- Factual claims must have citations pointing to verified sources.
- Empty citations are strictly prohibited UNLESS the statement explicitly
  declares "Insufficient evidence".
- Financial figures must be labeled "Directional estimate — not actuarial".
- The AI never auto-approves: all briefs are flagged for human sign-off.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, field_validator, model_validator


class Citation(BaseModel):
    """Citation linking a factual statement back to a verified source URL."""
    claim: str = Field(
        ...,
        description="The specific factual assertion or data point being cited."
    )
    source_url: str = Field(
        ...,
        description="Verified URL or internal table reference supporting the claim."
    )
    source_type: str = Field(
        ...,
        description="Type of source: 'competitor', 'regulatory', or 'internal_analytics'."
    )


class BriefEvidence(BaseModel):
    """A synthesized evidence section with mandatory citations.

    Architecture Rule: Citations can ONLY be empty if the statement
    is 'Insufficient evidence' — never invent un-sourced facts.
    """
    statement: str = Field(
        ...,
        description="Synthesized finding, market observation, or regulatory requirement."
    )
    citations: List[Citation] = Field(
        default_factory=list,
        description="List of verified citations backing this statement."
    )

    @model_validator(mode="after")
    def validate_citations_present_unless_insufficient(self) -> BriefEvidence:
        stmt_lower = self.statement.strip().lower()
        is_insufficient = stmt_lower.startswith("insufficient evidence") or stmt_lower == "insufficient evidence"
        if not self.citations and not is_insufficient:
            raise ValueError(
                f"Validation Error: Statement '{self.statement}' lacks citations. "
                "Citations can only be empty if statement begins with 'Insufficient evidence'."
            )
        return self


class DirectionalEstimate(BaseModel):
    """Financial impact estimate labeled strictly as directional.

    Architecture Rule: Never presented as a real actuarial rate.
    """
    range_low: float = Field(
        ...,
        description="Lower bound of directional loss/premium estimate in USD."
    )
    range_high: float = Field(
        ...,
        description="Upper bound of directional loss/premium estimate in USD."
    )
    label: str = Field(
        default="Directional estimate — not actuarial",
        description="Mandatory disclaimer label.",
        frozen=True,
    )
    basis: Optional[str] = Field(
        default=None,
        description="Summary of historical claim volumes and averages used to derive the range."
    )
    incident_count: Optional[int] = Field(
        default=None,
        description="Projected claim count behind the range (next 12 months)."
    )


from datetime import datetime


class ExternalMarketEvidence(BaseModel):
    """External market intelligence evidence item with mandatory verified source URL and timestamp."""
    source_name: str = Field(
        ...,
        description="Name of carrier, institution, regulatory body, or publisher."
    )
    product_or_initiative_name: str = Field(
        ...,
        description="Name of insurance product, coverage rider, or regulatory notice."
    )
    category: str = Field(
        ...,
        description="Category classification: 'news_article', 'research_report', or 'competitor_offering'."
    )
    summary: str = Field(
        ...,
        description="Qualitative summary of coverage terms, market position, or statutory mandate."
    )
    url: str = Field(
        ...,
        description="Mandatory verified HTTP/HTTPS source URL supporting the evidence."
    )
    source_type: str = Field(
        ...,
        description="Classification: 'competitor', 'regulatory', 'industry_report', 'news', or 'general'."
    )
    is_insurance_related: bool = Field(
        default=False,
        description="Deterministic boolean indicating whether finding is insurance-related."
    )
    date_retrieved: str = Field(
        default_factory=lambda: datetime.utcnow().isoformat(),
        description="Mandatory ISO 8601 timestamp of when the evidence was retrieved."
    )

    @field_validator("category", mode="before")
    @classmethod
    def validate_category(cls, v: Any) -> str:
        if not v or not isinstance(v, str):
            return "articles"
        v_clean = v.strip().lower()
        if "blog" in v_clean or "opinion" in v_clean or "perspective" in v_clean or "commentary" in v_clean:
            return "blogs"
        if "gov" in v_clean or "statut" in v_clean or "agency" in v_clean or "doi" in v_clean or "naic" in v_clean or "nhtsa" in v_clean or "cpsc" in v_clean or "osha" in v_clean or "federal" in v_clean or "state" in v_clean or "regulat" in v_clean:
            return "government_data"
        if "paper" in v_clean or "study" in v_clean or "whitepaper" in v_clean or "academic" in v_clean or "actuarial" in v_clean or "journal" in v_clean or "research" in v_clean:
            return "research_papers"
        if "competitor" in v_clean or "offering" in v_clean or "product" in v_clean or "carrier" in v_clean:
            return "competitor_offering"
        if "news" in v_clean or "article" in v_clean or "press" in v_clean:
            return "articles"
        return v_clean


class ProductBrief(BaseModel):
    """Full Product Decision Brief synthesized across all five domains.

    Presented to human Product Managers and Actuaries for review and sign-off
    prior to any export to Guidewire Advanced Product Designer (APD).
    """
    title: str = Field(
        ...,
        max_length=150,
        description="Title of the prospective insurance product or coverage endorsement."
    )
    tag_value: Optional[str] = Field(
        default=None,
        description="The underlying risk tag or loss cause analyzed if matched."
    )
    match_confidence: Optional[float] = Field(
        default=None,
        description="Confidence score (0.0 to 1.0) of the risk tag matching step."
    )
    analysis_basis: str = Field(
        default="direct",
        description="What the internal claims numbers describe: 'direct' (own risk pattern), 'proxy' (related patterns), "
                    "'line_baseline' (whole line of business) or 'none'."
    )
    proxy_tags: List[str] = Field(
        default_factory=list,
        description="Related risk patterns pooled as proxy claims history when the product has none of its own."
    )
    idea_context: Optional[str] = Field(
        default=None,
        max_length=4000,
        description="The product manager's own description of the idea (from the idea assistant), used as background only."
    )
    problem_statement: str = Field(
        ...,
        description="High-level summary of the market opportunity or coverage gap."
    )
    internal_evidence: List[BriefEvidence] = Field(
        default_factory=list,
        description="Evidence derived from verified internal claims/policies database."
    )
    competitor_comparison: List[BriefEvidence] = Field(
        default_factory=list,
        description="Synthesized competitor offerings with real source citations."
    )
    regulatory_notes: List[BriefEvidence] = Field(
        default_factory=list,
        description="Applicable insurance department bulletins and statutory requirements."
    )
    external_market_evidence: List[ExternalMarketEvidence] = Field(
        default_factory=list,
        description="Live web-researched market evidence items with verified URLs."
    )
    external_market_status: str = Field(
        default="offline",
        description="Status of external live web research: 'success', 'offline', or 'error'."
    )
    external_market_error_message: Optional[str] = Field(
        default=None,
        description="Specific error or offline banner message when external live search is not active."
    )
    directional_estimate: DirectionalEstimate = Field(
        ...,
        description="Directional financial exposure/opportunity estimate."
    )
    recommendation: str = Field(
        ...,
        description="Strategic recommendation for the product committee (Build / Endorse / Exclude / Monitor)."
    )
    claims_analytics: Dict[str, Any] = Field(
        default_factory=dict,
        description="Full structured claims analytics behind the 11 sections (for charts); computed, never generated."
    )
    claims_kpis: Dict[str, Any] = Field(
        default_factory=dict,
        description="Headline claims metrics computed by backend.analytics (never by the LLM)."
    )
    generation_method: str = Field(
        default="anthropic_claude",
        description="Generation engine used: 'anthropic_claude' or 'offline_deterministic_fallback'"
    )
    human_approval_required: bool = Field(
        default=True,
        description="Enforces human sign-off requirement before APD mapping.",
        frozen=True,
    )
