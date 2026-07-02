# Roadmap — 50 days, in public

Building theReviewMan in public, one day at a time. Progress is tracked by **day number, not calendar date** — slips move the schedule, never break it. Every day gets a LinkedIn post.

## Phase 1 · Foundation (Days 1–7)

- [x] **Day 1** — Public repo, README, architecture doc, this roadmap
- [x] **Day 1** — Project scaffold: package layout, `uv` + `pyproject.toml`, ruff/mypy/pytest wired
- [x] **Day 1** — Core review data models (Pydantic v2) with passing tests
- [ ] **Day 3** — Config module + FastAPI app skeleton
- [ ] **Day 6** — GitHub client: resolve PR URL, fetch metadata + PR diff via PyGithub
- [ ] **Day 7** — Smart diff chunking: split by file/hunk, preserve line numbers, handle huge PRs

## Phase 2 · Core build (Days 8–21)

- [ ] LangGraph pipeline: graph wiring, `AgentState`, node skeletons
- [ ] Structured-output enforcement — findings via JSON schema / tool calls, never prose
- [ ] Prompt module — versioned prompts in the repo like code
- [ ] Aggregation + dedupe of overlapping findings
- [ ] Verdict logic — severity-weighted decision with written reasoning
- [ ] Dedicated security pass (injection, secrets, auth, deserialization)
- [ ] Failure handling + retries
- [ ] Step-level tracing: model, tokens, latency per node
- [ ] End-to-end CLI: `review <pr-url>`
- [ ] Tag **v0.1**

## Phase 3 · Ship v1 (Days 22–28)

- [ ] Next.js + Tailwind UI
- [ ] Wire UI to the API
- [ ] Docker deploy
- [ ] Live public demo
- [ ] Polished UX pass
- [ ] 90-second demo video

## Phase 4 · Depth & evaluation (Days 29–42)

- [ ] Human-labeled PR dataset
- [ ] Eval harness: precision/recall per category
- [ ] Publish baseline numbers
- [ ] Targeted improvements with before/after metrics
- [ ] Unit tests + CI (GitHub Actions)
- [ ] Caching + cost tracking
- [ ] Post-review-to-PR mode: comment directly on the pull request
- [ ] Tag **v1.0**

## Phase 5 · Signal (Days 43–50)

- [ ] Technical write-up
- [ ] good-first-issues + CONTRIBUTING.md
- [ ] Case-study carousel
- [ ] Retrospective: 50 days, what worked, what didn't
