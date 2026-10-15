# 028 — MCP server for 1Password or Vault with least-privilege scopes

This folder is a runnable, dependency-free reference implementation of the project's core control pattern. Connect the vendor-specific adapters listed below when you move from classroom demo to deployment.

## Architecture

`agent tool call → scope + typed handler → audited result`

## Suggested production stack

Python · MCP SDK · typed tools · audit log

## Implementation steps

1. Define the contract for agent tool call; include IDs, event time, and ownership.
2. Create the smallest adapter that reads agent tool call without hiding failures.
3. Implement issue short-lived secret reads only for approved paths and never return values to logs.
4. Write audited result idempotently and attach a run or trace identifier.
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
