"""Held-out governance scenarios for F124."""
from safety.policy import REQUIRED_REVIEWS, authorize


def base():
    return {key: True for key in REQUIRED_REVIEWS}


SCENARIOS = [
    ({}, False),
    (base(), True),
    (base() | {"unsupported_claim": True}, False),
    (base() | {"impersonation_risk": True}, False),
    (base() | {"harassment_risk": True}, False),
    (base() | {"deceptive_engagement": True}, False),
    (base() | {"privacy_consent_gap": True}, False),
    (base() | {"copyright_rights_gap": True}, False),
    (base() | {"legal_reputation_risk": True}, False),
    (base() | {"evidence_provenance_gap": True}, False),
]


def main():
    for index, (context, expected) in enumerate(SCENARIOS, 1):
        actual = authorize("release_support_package", context)["allowed"]
        assert actual is expected, f"scenario {index}: expected {expected}, got {actual}"
    print(f"F124 held-out governance: {len(SCENARIOS)}/{len(SCENARIOS)} passed")


if __name__ == "__main__":
    main()
