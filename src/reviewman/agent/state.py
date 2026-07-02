"""LangGraph agent state — the single dict threaded through every pipeline node.

Wired into the graph on Day 8 — follow the roadmap.
"""

from typing import Any, TypedDict

from reviewman.models import Finding, Review, StepTrace

DiffChunk = Any  # placeholder — the DiffChunk model lands Day 7


class AgentState(TypedDict):
    pr_url: str
    repo_full_name: str
    pr_number: int
    pr_meta: dict  # title, author, base/head, files changed
    chunks: list[DiffChunk]
    chunk_findings: list[Finding]
    security_findings: list[Finding]
    findings: list[Finding]  # aggregated + deduped
    review: Review | None
    errors: list[str]
    trace: list[StepTrace]
