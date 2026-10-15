"""Project 56: Centralize DLP policies across Google Drive, S3, and."""
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from hashlib import sha256
import json

TITLE = "Centralize DLP policies across Google Drive, S3, and Postgres"
FOCUS = (
    "evaluate one rule model consistently across cloud storage and "
    "database connectors"
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
    return apply(Change("teacher", "execute-project-56", approved=True))

if __name__ == "__main__":
    print(json.dumps(run_demo(), indent=2))
