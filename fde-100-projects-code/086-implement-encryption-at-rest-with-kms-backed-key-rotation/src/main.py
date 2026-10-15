"""Project 86: encryption at rest."""
from dataclasses import asdict, dataclass
from hashlib import sha256
import json

TITLE = "Implement encryption at rest with KMS-backed key rotation"
FOCUS = (
    "encrypt with a data key, wrap it with KMS, and rotate the "
    "wrapping key safely"
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
    request = Request("student", "read", "project-86", frozenset({"trained"}))
    return decide(request)

if __name__ == "__main__":
    print(json.dumps(run_demo(), indent=2))
