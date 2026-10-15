"""Project 96: Compliance copilot."""
from dataclasses import asdict, dataclass
import json

TITLE = "Compliance copilot that maps controls to evidence and gaps"
FOCUS = (
    "retrieve control evidence, identify coverage gaps, and keep "
    "every recommendation cited"
)
FLOW = ["user intent","tools + controls","reviewable outcome"]

@dataclass(frozen=True)
class Action:
    tool: str
    arguments: dict[str, object]
    requires_approval: bool = True

def plan(user_request: str) -> list[Action]:
    if not user_request.strip():
        raise ValueError("the user request cannot be empty")
    return [
        Action("retrieve_context", {"query": user_request}, False),
        Action("propose_outcome", {"focus": FOCUS}, True),
    ]

def execute(actions: list[Action], approved: bool) -> list[dict[str, object]]:
    results = []
    for action in actions:
        if action.requires_approval and not approved:
            results.append({"tool": action.tool, "status": "waiting"})
            continue
        results.append({"tool": action.tool, "status": "complete"})
    return results

def run_demo() -> dict[str, object]:
    actions = plan("teach project 96")
    return {"plan": [asdict(item) for item in actions],
            "results": execute(actions, approved=False)}

if __name__ == "__main__":
    print(json.dumps(run_demo(), indent=2))
