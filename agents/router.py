from utils.json_parser import parse_json
from utils.gemini_client import ask_gemini


def route_request(plan: dict):
    prompt = f"""
You are an AI Request Router.

Based on the execution plan below, assign the request to the most appropriate support team.

Execution Plan:
{plan}

The assigned team should be one of these:
- Billing Support Team
- Technical Support Team
- Customer Care Team
- Escalation Team

Return ONLY valid JSON in EXACTLY this format.

{{
    "assigned_team": "...",
    "ticket_status": "...",
    "estimated_resolution": "...",
    "next_step": "..."
}}

Do not return any explanation.
Do not change the JSON keys.
"""

    response = ask_gemini(prompt)
    return parse_json(response)