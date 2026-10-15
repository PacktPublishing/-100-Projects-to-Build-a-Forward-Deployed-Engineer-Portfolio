"""Project 1: Ingest messy public CSVs into a clean Parquet lake."""
from collections.abc import Iterable, Mapping
from datetime import UTC, datetime
from hashlib import sha256
import json

TITLE = (
    "Ingest messy public CSVs into a clean Parquet lake with schema "
    "validation"
)
FOCUS = (
    "normalize headers, coerce types, quarantine bad rows, and write "
    "partitioned Parquet"
)
FLOW = ["messy CSV","schema gate","Parquet lake"]

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
    return run([{"source": FLOW[0], "value": 1}])

if __name__ == "__main__":
    print(json.dumps(run_demo(), indent=2))
