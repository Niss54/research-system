"""
Nissh Research System v2 - Data Contracts & Schemas
===================================================
Zero-dependency typed models using standard Python dataclasses.
Provides robust JSON serialization, deserialization, and schema validation.
"""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Optional
import json

@dataclass
class P1ValidationHandoff:
    problem_statement: str = ""
    target_audience: str = ""
    frequency: str = "Daily"  # Daily, Weekly, Monthly, Rarely
    frequency_evidence: List[str] = field(default_factory=list)
    severity: int = 8  # 1-10
    severity_evidence: List[str] = field(default_factory=list)
    willingness_to_pay: str = "Yes"  # Yes, Partial, No
    wtp_evidence: List[str] = field(default_factory=list)
    key_sources: List[Dict[str, str]] = field(default_factory=list)
    verdict: str = "GO"  # GO, MAYBE, NO-GO
    verdict_reasoning: str = ""
    key_pain_signals: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "P1ValidationHandoff":
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


@dataclass
class CompetitorItem:
    name: str = ""
    url: str = ""
    category: str = "Direct"  # Direct, Indirect, Workaround
    pricing: str = ""
    target_user: str = ""
    key_features: List[str] = field(default_factory=list)
    limitations: str = ""
    is_live: bool = True
    http_status: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class P2LandscapeHandoff:
    problem_space: str = ""
    target_audience: str = ""
    competitors: List[CompetitorItem] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["competitors"] = [c if isinstance(c, dict) else c.to_dict() for c in self.competitors]
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "P2LandscapeHandoff":
        comps = [CompetitorItem(**c) if isinstance(c, dict) else c for c in data.get("competitors", [])]
        return cls(
            problem_space=data.get("problem_space", ""),
            target_audience=data.get("target_audience", ""),
            competitors=comps
        )


@dataclass
class CompetitorTeardown:
    name: str = ""
    url: str = ""
    type: str = "Direct"
    summary: str = ""
    pricing_tiers: str = ""
    what_users_love: List[str] = field(default_factory=list)
    what_users_hate: List[str] = field(default_factory=list)
    critical_gaps: str = ""
    this_tool_does_not: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class P3ResearchHandoff:
    profiles: List[CompetitorTeardown] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {"profiles": [p.to_dict() if hasattr(p, "to_dict") else p for p in self.profiles]}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "P3ResearchHandoff":
        profs = [CompetitorTeardown(**p) if isinstance(p, dict) else p for p in data.get("profiles", [])]
        return cls(profiles=profs)


@dataclass
class GapItem:
    id: int = 1
    name: str = ""
    category: str = "Workflow Gap"
    description: str = ""
    pain_score: float = 5.0
    market_score: float = 4.0
    feasibility_score: float = 4.0
    opportunity_score: float = 8.5
    justification: str = ""
    key_differentiator: str = ""

    def calculate_score(self) -> float:
        """Standard Nissh Opportunity Formula: (Pain * Market * Feasibility) / 2 normalized to 10 max"""
        raw = (self.pain_score * self.market_score * self.feasibility_score) / 2.0
        # Normalize: if max is 5*5*5/2 = 62.5, score out of 10
        self.opportunity_score = round(min(10.0, (raw / 62.5) * 10.0), 2)
        return self.opportunity_score

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class P4GapAnalysisHandoff:
    top_5_gaps: List[GapItem] = field(default_factory=list)
    recommended_wedge: Optional[GapItem] = None
    feature_matrix: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "top_5_gaps": [g.to_dict() if hasattr(g, "to_dict") else g for g in self.top_5_gaps],
            "recommended_wedge": self.recommended_wedge.to_dict() if self.recommended_wedge else None,
            "feature_matrix": self.feature_matrix
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "P4GapAnalysisHandoff":
        gaps = [GapItem(**g) if isinstance(g, dict) else g for g in data.get("top_5_gaps", [])]
        wedge_raw = data.get("recommended_wedge")
        wedge = GapItem(**wedge_raw) if isinstance(wedge_raw, dict) else None
        return cls(
            top_5_gaps=gaps,
            recommended_wedge=wedge,
            feature_matrix=data.get("feature_matrix", {})
        )


@dataclass
class VerifiedGapItem:
    name: str = ""
    verdict: str = "CONFIRMED"  # CONFIRMED, PARTIAL, FALSE
    evidence: str = ""
    why_unbuilt: str = ""
    why_now: str = ""
    mvp_features: List[str] = field(default_factory=list)
    source_links: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class P5VerifyGapsHandoff:
    verified_gaps: List[VerifiedGapItem] = field(default_factory=list)
    primary_opportunity: str = ""
    core_value_prop: str = ""
    mvp_build_scope: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "verified_gaps": [vg.to_dict() if hasattr(vg, "to_dict") else vg for vg in self.verified_gaps],
            "primary_opportunity": self.primary_opportunity,
            "core_value_prop": self.core_value_prop,
            "mvp_build_scope": self.mvp_build_scope
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "P5VerifyGapsHandoff":
        vgaps = [VerifiedGapItem(**vg) if isinstance(vg, dict) else vg for vg in data.get("verified_gaps", [])]
        return cls(
            verified_gaps=vgaps,
            primary_opportunity=data.get("primary_opportunity", ""),
            core_value_prop=data.get("core_value_prop", ""),
            mvp_build_scope=data.get("mvp_build_scope", [])
        )


@dataclass
class P6DiligenceHandoff:
    project_name_proposal: str = ""
    one_line_pitch: str = ""
    problem_statement: str = ""
    target_audience_icp: str = ""
    core_differentiator: str = ""
    mvp_core_features: List[str] = field(default_factory=list)
    tech_stack_suggestion: str = ""
    competitive_moat: str = ""
    launch_plan_30_day: List[Dict[str, str]] = field(default_factory=list)
    full_memo_markdown: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "P6DiligenceHandoff":
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


@dataclass
class P7LaunchHandoff:
    readme_content: str = ""
    tagline: str = ""
    project_name: str = ""
    badges: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "P7LaunchHandoff":
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})
