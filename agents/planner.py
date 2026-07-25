from utils.json_parser import parse_json
from utils.gemini_client import ask_gemini

def plan_actions(classification: dict):
    prompt = f"""
You are an AI Workflow Planner.

Based on the classification below, generate an execution plan for a customer support workflow.

Classification:
{classification}

Return ONLY valid JSON.

Example:

{{
    "department": "Billing Team",
    "priority": "High",
    "actions": [
        "Create support ticket",
        "Assign to Billing Team",
        "Send acknowledgement email",
        "Set SLA to 24 hours"
    ]
}}
"""
    response=ask_gemini(prompt)
    return parse_json(response)



# def plan_actions(workflow: dict):
#     return workflow["plan"]
