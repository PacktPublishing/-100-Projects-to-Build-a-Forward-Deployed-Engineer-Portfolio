# 004 — Streaming ingest from Kafka to Delta Lake with watermarking and compaction

This folder is a runnable, dependency-free reference implementation of the project's core control pattern. Connect the vendor-specific adapters listed below when you move from classroom demo to deployment.

## Architecture

`Kafka events → watermark + state → Delta Lake`

## Suggested production stack

PySpark · Kafka · Delta Lake

## Implementation steps

1. Define the contract for Kafka events; include IDs, event time, and ownership.
2. Create the smallest adapter that reads Kafka events without hiding failures.
3. Implement parse Kafka events, apply an event-time watermark, write Delta, and compact small files.
4. Write Delta Lake idempotently and attach a run or trace identifier.
5. Test duplicates, malformed input, retries, authorization, and replay before deployment.

## Run the safe demo

```bash
python3 src/main.py
python3 -m unittest discover -s tests
```

## Production extension checklist

- Replace the in-memory adapter with the named platform SDK or a small HTTP boundary.
- Load secrets from environment variables or a secrets manager; never commit them.
- Persist idempotency, checkpoint, audit, or state records in a durable store.
- Add contract tests, failure injection, telemetry, least-privilege scopes, and a rollback path.
