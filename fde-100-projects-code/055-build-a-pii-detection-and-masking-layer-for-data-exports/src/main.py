"""Project 55: PII detection and masking layer for data exports."""
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from hashlib import sha256
import json

TITLE = "Build a PII detection and masking layer for data exports"
FOCUS = (
    "classify sensitive fields and apply irreversible or reversible "
    "masking by policy"
)
FLOW = ["enterprise event","policy + workflow","evidence + action"]

@dataclass(frozen=True)
class Change:
    actor: str
    action: str
    approved: bool

def apply(change: Change, previous_hash: str = "GENESIS") -> dict[str, object]:
    if not change.approved:
        raise PermissionError("approval gate rejected the change")
    event = {
        "project": TITLE,
        "change": asdict(change),
        "timestamp": datetime.now(UTC).isoformat(),
        "previous_hash": previous_hash,
    }
    encoded = json.dumps(event, sort_keys=True).encode()
    event["event_hash"] = sha256(encoded).hexdigest()
    return event

def run_demo() -> dict[str, object]:
    return apply(Change("teacher", "execute-project-55", approved=True))

if __name__ == "__main__":
    print(json.dumps(run_demo(), indent=2))
