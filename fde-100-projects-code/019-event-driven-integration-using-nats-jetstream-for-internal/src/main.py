"""Project 19: Event-driven integration."""
from dataclasses import dataclass
from hashlib import sha256
import json
import time

TITLE = (
    "Event-driven integration using NATS JetStream for internal "
    "services"
)
FOCUS = (
    "publish durable events, acknowledge only after work succeeds, "
    "and replay safely"
)
FLOW = ["client request","contract + resilience","normalized response"]

@dataclass(frozen=True)
class Request:
    idempotency_key: str
    payload: dict[str, object]

class Gateway:
    def __init__(self) -> None:
        self.cache: dict[str, dict[str, object]] = {}

    def handle(self, request: Request) -> dict[str, object]:
        if not request.idempotency_key:
            raise ValueError("idempotency key is required")
        if request.idempotency_key in self.cache:
            return self.cache[request.idempotency_key]
        canonical = {str(k).lower(): v for k, v in request.payload.items()}
        digest = sha256(json.dumps(canonical, sort_keys=True).encode()).hexdigest()[:12]
        result = {"id": digest, "data": canonical, "flow": FLOW}
        self.cache[request.idempotency_key] = result
        return result

def run_demo() -> dict[str, object]:
    gateway = Gateway()
    request = Request(f"demo-19", {"VendorID": 19})
    started = time.perf_counter()
    result = gateway.handle(request)
    result["latency_ms"] = round((time.perf_counter() - started) * 1000, 3)
    return result

if __name__ == "__main__":
    print(json.dumps(run_demo(), indent=2))
