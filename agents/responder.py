from utils.json_parser import parse_json
from utils.gemini_client import ask_gemini

def generate_response(request: str, classification: dict, plan: dict, routing: dict):
    prompt=f"""
You are an AI Customer Support Assistant.

Customer Request:
{request}

Classification:
{classification}

Execution plan:
{plan}

Routing Details:
{routing}

Generate a professional, empathetic customer support response.
Maintain a professional and empathetic tone.

The response should:

- acknowledge the issue
- explain the next steps
- mention the assigned team
- mention the estimated resolution if available

Return ONLY valid JSON.

{{
    "subject": "...",
    "customer_message": "..."
}}
"""
    response=ask_gemini(prompt)
    return parse_json(response)


# def generate_response(workflow: dict):
#     return workflow["response"]
