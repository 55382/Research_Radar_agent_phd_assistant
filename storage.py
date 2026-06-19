import json
import os

DATA_FILE = "logs/papers.jsonl"
FEEDBACK_FILE = "logs/feedback.jsonl"


def save_papers(papers):
    os.makedirs("logs", exist_ok=True)
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        for p in papers:
            f.write(json.dumps(p) + "\n")


def load_papers():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return [json.loads(x) for x in f]