import json

def parse_json(text: str):
    """
    Extracts JSON even if Gemini wraps it in ```json ... ```
    """
    text=text.strip()
    if text.startswith("```json"):
        text=text.replace("```json", "", 1)
    if text.startswith("```"):
        text = text.replace("```", "", 1)

    if text.endswith("```"):
        text = text[:-3]

    return json.loads(text.strip())