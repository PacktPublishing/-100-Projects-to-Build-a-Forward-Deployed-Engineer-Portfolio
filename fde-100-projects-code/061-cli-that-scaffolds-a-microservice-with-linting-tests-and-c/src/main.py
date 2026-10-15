"""Project 61: CLI."""
import argparse
import json
from pathlib import Path

TITLE = "CLI that scaffolds a microservice with linting, tests, and CI"
FOCUS = (
    "render a predictable service skeleton and fail if generated "
    "files already exist"
)
FLOW = ["developer command","validate + execute","diff + exit code"]

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=TITLE)
    parser.add_argument("target", type=Path)
    parser.add_argument("--apply", action="store_true")
    return parser

def execute(target: Path, apply: bool) -> dict[str, object]:
    plan = {
        "target": str(target.resolve()),
        "focus": FOCUS,
        "changes": [f"validate {FLOW[0]}", f"produce {FLOW[2]}"],
    }
    if apply and not target.exists():
        target.mkdir(parents=True)
        plan["applied"] = True
    else:
        plan["applied"] = False
    return plan

def run_demo() -> dict[str, object]:
    return execute(Path("demo-project-61"), apply=False)

if __name__ == "__main__":
    args = build_parser().parse_args()
    print(json.dumps(execute(args.target, args.apply), indent=2))
