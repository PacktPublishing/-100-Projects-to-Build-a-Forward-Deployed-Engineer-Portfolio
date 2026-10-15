"""Project 41: End-to-end RAG evaluation framework."""
from dataclasses import dataclass
from statistics import fmean
import json
import time

TITLE = "End-to-end RAG evaluation framework with golden datasets"
FOCUS = (
    "run the same questions against a frozen corpus and compare with "
    "golden expectations"
)
FLOW = ["traces + examples","score + compare","quality decision"]

@dataclass(frozen=True)
class Example:
    expected: set[str]
    observed: set[str]
    latency_ms: float

def recall(example: Example) -> float:
    return len(example.expected & example.observed) / max(1, len(example.expected))

def evaluate(examples: list[Example]) -> dict[str, float | bool]:
    started = time.perf_counter()
    recalls = [recall(example) for example in examples]
    latencies = [example.latency_ms for example in examples]
    result = {
        "recall": round(fmean(recalls), 3),
        "latency_ms": round(fmean(latencies), 1),
        "evaluation_ms": round((time.perf_counter() - started) * 1000, 3),
    }
    result["passed"] = result["recall"] >= 0.8
    return result

def run_demo() -> dict[str, float | bool]:
    return evaluate([Example({"a", "b"}, {"a", "b", "p41"}, 42.0)])

if __name__ == "__main__":
    print(json.dumps(run_demo(), indent=2))
