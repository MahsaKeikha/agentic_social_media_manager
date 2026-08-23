"""Fail-closed governance for F124 Agentic Social Media Manager."""

PROTECTED_ACTIONS = {
    "publish_post",
    "publish_reply",
    "send_direct_message",
    "launch_campaign",
    "delete_public_content",
    "external_distribution",
}

REQUIRED_REVIEWS = (
    "strategy_reviewed",
    "content_reviewed",
    "community_reviewed",
    "claims_reviewed",
    "privacy_consent_reviewed",
    "legal_reputation_reviewed",
    "evidence_provenance_reviewed",
    "qualified_social_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "binding social-media action is outside reference-system scope"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required social-media review", "missing": missing}

    blockers = []
    checks = {
        "unsupported_claim": "claim exceeds reviewed evidence",
        "impersonation_risk": "identity or impersonation risk unresolved",
        "harassment_risk": "harassment or abusive-engagement risk unresolved",
        "deceptive_engagement": "deceptive or manipulated engagement detected",
        "privacy_consent_gap": "privacy, consent, or personal-data gap unresolved",
        "copyright_rights_gap": "copyright, licensing, or media-rights gap unresolved",
        "legal_reputation_risk": "legal or reputational risk unresolved",
        "evidence_provenance_gap": "evidence provenance incomplete",
    }
    for key, message in checks.items():
        if context.get(key):
            blockers.append(message)

    if blockers:
        return {"allowed": False, "reason": "social-media governance blocker", "blockers": blockers}
    return {"allowed": True, "reason": "social-media support package approved after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS
