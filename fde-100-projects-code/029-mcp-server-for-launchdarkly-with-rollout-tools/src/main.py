"""Project 29: MCP server for LaunchDarkly."""
from dataclasses import dataclass
from datetime import UTC, datetime
import json

TITLE = "MCP server for LaunchDarkly with rollout tools"
FOCUS = (
    "preview a rollout plan, validate targeting, and require "
    "confirmation before mutation"
)
FLOW = ["agent tool call","scope + typed handler","audited result"]

REQUIRED_SCOPE = "project:29:read"

@dataclass(frozen=True)
class ToolCall:
    actor: str
    scopes: frozenset[str]
    arguments: dict[str, object]

def invoke(call: ToolCall) -> dict[str, object]:
    if REQUIRED_SCOPE not in call.scopes:
        raise PermissionError(f"missing scope: {REQUIRED_SCOPE}")
    if not call.arguments:
        raise ValueError("typed tool arguments cannot be empty")
    result = {"status": "ok", "flow": FLOW, "data": call.arguments}
    audit = {
        "actor": call.actor,
        "tool": TITLE,
        "at": datetime.now(UTC).isoformat(),
        "wrote_secret": False,
    }
    return {"result": result, "audit": audit}

def run_demo() -> dict[str, object]:
    call = ToolCall("teacher", frozenset({REQUIRED_SCOPE}), {"limit": 3})
    return invoke(call)

if __name__ == "__main__":
    print(json.dumps(run_demo(), indent=2))
