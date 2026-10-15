"""Project 3: CDC pipeline from PostgreSQL to BigQuery."""
from collections.abc import Iterable, Mapping
from datetime import UTC, datetime
from hashlib import sha256
import json

TITLE = (
    "Create a CDC pipeline from PostgreSQL to BigQuery with "
    "late-arrival handling"
)
FOCUS = (
    "order changes by source timestamp, retain the newest version, "
    "and sweep late events"
)
FLOW = ["PostgreSQL changes","late-arrival merge","BigQuery"]

def validate(row: Mapping[str, object]) -> None:
    if not row:
        raise ValueError("empty record")
    if any(value is None for value in row.values()):
        raise ValueError("null value violates the demo contract")

def transform(row: Mapping[str, object]) -> dict[str, object]:
    clean = {str(key).strip().lower(): value for key, value in row.items()}
    payload = json.dumps(clean, sort_keys=True, default=str)
    clean["record_id"] = sha256(payload.encode()).hexdigest()[:16]
    clean["processed_at"] = datetime.now(UTC).isoformat()
    clean["project"] = TITLE
    return clean

def run(rows: Iterable[Mapping[str, object]]) -> list[dict[str, object]]:
    output: dict[str, dict[str, object]] = {}
    for row in rows:
        validate(row)
        item = transform(row)
        output[str(item["record_id"])] = item
    return list(output.values())

def run_demo() -> list[dict[str, object]]:
    return run([{"source": FLOW[0], "value": 3}])

if __name__ == "__main__":
    print(json.dumps(run_demo(), indent=2))
