from AGENTS import community_agent, content_agent, measurement_agent, review_agent, strategy_agent
from safety.policy import authorize


def run(case: dict) -> dict:
    """Run social specialists and apply the fail-closed release gate."""
    result = {
        "strategy": strategy_agent.run(case),
        "content": content_agent.run(case),
        "community": community_agent.run(case),
        "measurement": measurement_agent.run(case),
        "review": review_agent.run(case),
    }
    governance = authorize("release_support_package", case.get("governance", {}))
    result["governance"] = governance
    result["released"] = governance["allowed"]
    return result
