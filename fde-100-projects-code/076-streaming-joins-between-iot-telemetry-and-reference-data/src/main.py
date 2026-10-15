"""Project 76: Streaming joins between IoT telemetry and reference."""
from collections import defaultdict
from dataclasses import dataclass
import asyncio
import json

TITLE = "Streaming joins between IoT telemetry and reference data"
FOCUS = (
    "join telemetry to slowly changing reference data using a bounded "
    "temporal lookup"
)
FLOW = ["event stream","event-time state","live output"]

@dataclass(frozen=True)
class Event:
    key: str
    event_time: int
    value: float

async def process(events: list[Event], allowed_lateness: int = 5) -> dict[str, float]:
    state: defaultdict[str, float] = defaultdict(float)
    watermark = -1
    for event in sorted(events, key=lambda item: item.event_time):
        watermark = max(watermark, event.event_time - allowed_lateness)
        if event.event_time < watermark:
            continue
        state[event.key] += event.value
        await asyncio.sleep(0)
    return dict(state)

def run_demo() -> dict[str, float]:
    events = [Event("project-76", 10, 1.0), Event("project-76", 12, 2.0)]
    return asyncio.run(process(events))

if __name__ == "__main__":
    print(json.dumps(run_demo(), indent=2))
