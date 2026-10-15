"""Project 37: RAG evaluation harness for recall, precision,."""
from dataclasses import dataclass
import json
import math
import re

TITLE = (
    "Build a RAG evaluation harness for recall, precision, "
    "faithfulness, and latency"
)
FOCUS = (
    "calculate retrieval and answer metrics on a repeatable dataset "
    "with latency tracking"
)
FLOW = ["question + corpus","retrieve + reason","grounded answer"]

@dataclass(frozen=True)
class Document:
    id: str
    text: str

def tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))

def score(query: str, document: Document) -> float:
    left, right = tokens(query), tokens(document.text)
    return len(left & right) / math.sqrt(max(1, len(left) * len(right)))

def retrieve(query: str, corpus: list[Document], k: int = 2) -> list[dict[str, object]]:
    ranked = sorted(corpus, key=lambda doc: score(query, doc), reverse=True)
    return [{"id": doc.id, "text": doc.text, "score": score(query, doc)}
            for doc in ranked[:k] if score(query, doc) > 0]

def run_demo() -> dict[str, object]:
    corpus = [Document("doc-1", FOCUS), Document("doc-2", TITLE)]
    evidence = retrieve("grounded project evidence", corpus)
    return {"answer": "Use only retrieved evidence.", "citations": evidence}

if __name__ == "__main__":
    print(json.dumps(run_demo(), indent=2))
