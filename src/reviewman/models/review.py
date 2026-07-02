"""Core review data models — the contract every pipeline node builds against."""

from enum import Enum

from pydantic import BaseModel, Field


class Category(str, Enum):
    bug = "bug"
    security = "security"
    quality = "quality"
    performance = "performance"


class Severity(str, Enum):
    critical = "critical"
    high = "high"
    medium = "medium"
    low = "low"


class Finding(BaseModel):
    category: Category
    severity: Severity
    file: str
    line_start: int
    line_end: int | None = None
    title: str
    explanation: str
    suggestion: str | None = None


class Verdict(str, Enum):
    approve = "approve"
    request_changes = "request_changes"
    comment = "comment"


class StepTrace(BaseModel):
    node: str
    model: str | None = None
    input_tokens: int = 0
    output_tokens: int = 0
    latency_ms: int = 0


class Review(BaseModel):
    pr_url: str
    summary: str
    findings: list[Finding] = Field(default_factory=list)
    verdict: Verdict
    verdict_reasoning: str
    trace: list[StepTrace] = Field(default_factory=list)
