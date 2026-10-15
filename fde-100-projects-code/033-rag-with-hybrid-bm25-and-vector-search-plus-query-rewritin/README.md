# 033 — RAG with hybrid BM25 and vector search plus query rewriting

This folder is a runnable, dependency-free reference implementation of the project's core control pattern. Connect the vendor-specific adapters listed below when you move from classroom demo to deployment.

## Architecture

`question + corpus → retrieve + reason → grounded answer`

## Suggested production stack

Python · BM25 · embeddings · rank fusion

## Implementation steps

1. Define the contract for question + corpus; include IDs, event time, and ownership.
2. Create the smallest adapter that reads question + corpus without hiding failures.
3. Implement merge lexical and semantic rankings after rewriting an ambiguous query.
4. Write grounded answer idempotently and attach a run or trace identifier.
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
