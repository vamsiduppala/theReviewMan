"""Round-trip tests for the core review models."""

from reviewman.models import Category, Finding, Review, Severity, StepTrace, Verdict


def make_finding() -> Finding:
    return Finding(
        category=Category.security,
        severity=Severity.critical,
        file="src/auth/session.py",
        line_start=42,
        line_end=48,
        title="Hardcoded API token in session handler",
        explanation="A bearer token is committed in plain text and shipped to every environment.",
        suggestion="Load the token from configuration and rotate the exposed credential.",
    )


def test_finding_round_trip() -> None:
    finding = make_finding()
    data = finding.model_dump()

    assert data["category"] == "security"
    assert data["severity"] == "critical"
    assert data["line_end"] == 48
    assert Finding(**data) == finding


def test_finding_optional_fields_default() -> None:
    finding = Finding(
        category=Category.quality,
        severity=Severity.low,
        file="src/utils.py",
        line_start=10,
        title="Dead code",
        explanation="This branch is unreachable.",
    )

    assert finding.line_end is None
    assert finding.suggestion is None


def test_review_round_trip() -> None:
    review = Review(
        pr_url="https://github.com/vamsiduppala/theReviewMan/pull/1",
        summary="One critical security issue; changes requested.",
        findings=[make_finding()],
        verdict=Verdict.request_changes,
        verdict_reasoning="A critical severity finding forces request_changes.",
        trace=[
            StepTrace(node="fetch_pr", latency_ms=210),
            StepTrace(
                node="analyze_chunks",
                model="claude-sonnet-4-6",
                input_tokens=1500,
                output_tokens=320,
                latency_ms=2400,
            ),
        ],
    )
    data = review.model_dump()

    assert data["verdict"] == "request_changes"
    assert data["findings"][0]["file"] == "src/auth/session.py"
    assert data["trace"][1]["model"] == "claude-sonnet-4-6"
    assert Review(**data) == review
    assert Review.model_validate(data) == review


def test_review_defaults_to_empty_lists() -> None:
    review = Review(
        pr_url="https://github.com/vamsiduppala/theReviewMan/pull/2",
        summary="Clean change.",
        verdict=Verdict.approve,
        verdict_reasoning="No findings above the approval threshold.",
    )

    assert review.findings == []
    assert review.trace == []
