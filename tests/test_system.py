from orchestration.orchestrator import run
from safety.policy import PROTECTED_ACTIONS, REQUIRED_REVIEWS, authorize


def approved_context():
    return {key: True for key in REQUIRED_REVIEWS}


def test_orchestrator_runs_five_agents_and_fails_closed():
    result = run({})
    for key in ("strategy", "content", "community", "measurement", "review"):
        assert key in result
    assert result["released"] is False


def test_missing_reviews_fail_closed():
    result = authorize("release_support_package", {})
    assert result["allowed"] is False
    assert len(result["missing"]) == 8


def test_reviewed_package_can_release():
    assert authorize("release_support_package", approved_context())["allowed"] is True


def test_impersonation_blocks():
    assert authorize("release_support_package", approved_context() | {"impersonation_risk": True})["allowed"] is False


def test_deceptive_engagement_blocks():
    assert authorize("release_support_package", approved_context() | {"deceptive_engagement": True})["allowed"] is False


def test_privacy_gap_blocks():
    assert authorize("release_support_package", approved_context() | {"privacy_consent_gap": True})["allowed"] is False


def test_unsupported_claim_blocks():
    assert authorize("release_support_package", approved_context() | {"unsupported_claim": True})["allowed"] is False


def test_protected_actions_never_autonomously_release():
    context = approved_context()
    for action in PROTECTED_ACTIONS:
        assert authorize(action, context)["allowed"] is False
