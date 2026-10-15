"""Project 88: compliant data-retention and deletion scheduler."""
from dataclasses import asdict, dataclass
from hashlib import sha256
import json

TITLE = "Create a compliant data-retention and deletion scheduler"
FOCUS = (
    "calculate policy deadlines, place records on legal hold, and "
    "verify deletion outcomes"
)
FLOW = ["subject + resource","policy decision","enforced + logged"]

@dataclass(frozen=True)
class Request:
    subject: str
    action: str
    resource: str
    attributes: frozenset[str]

def decide(request: Request) -> dict[str, object]:
    allow = "trained" in request.attributes and request.action != "delete-all"
    evidence = {"request": asdict(request), "allow": allow, "policy": TITLE}
    serializable = {**evidence, "request": {**asdict(request),
                    "attributes": sorted(request.attributes)}}
    encoded = json.dumps(serializable, sort_keys=True).encode()
    serializable["decision_hash"] = sha256(encoded).hexdigest()[:16]
    return serializable

def run_demo() -> dict[str, object]:
    request = Request("student", "read", "project-88", frozenset({"trained"}))
    return decide(request)

if __name__ == "__main__":
    print(json.dumps(run_demo(), indent=2))
