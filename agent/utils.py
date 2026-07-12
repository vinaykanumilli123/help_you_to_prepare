import json

def extract_json(text: str):
    text = text.strip()

    if text.startswith("```json"):
        text = text.removeprefix("```json").strip()

    if text.endswith("```"):
        text = text.removesuffix("```").strip()

    return json.loads(text)