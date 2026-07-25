from utils.json_parser import parse_json
from utils.gemini_client import ask_gemini

def classify_request(user_request: str):
    prompt=f"""
You are AI Customer Support Classifier.

Analyze the customer request below.
Customer Request:
{user_request}
Classify it into EXACTLY one of the categories:
- Complaint
- Service Request
- General Enquiry
- Escalation

Do not invent new categories.

Urgency should be one of:
- Low
- Medium
- High

Return ONLY valid JSON.
Example:
{{
    "category": "Complaint",
    "urgency": "High",
    "reason": "Customer reports duplicate payment."
}}
"""
    response=ask_gemini(prompt)
    return parse_json(response)


# from utils.json_parser import parse_json
# from utils.gemini_client import ask_gemini


# def run_workflow(user_request: str):
#     prompt = f"""
# You are an AI Customer Support Workflow Agent.

# Analyze the following customer request:

# Customer Request:
# {user_request}

# Perform ALL of the following tasks.

# 1. Classify the request.
# 2. Create an execution plan.
# 3. Decide routing.
# 4. Generate a professional customer response.

# Return ONLY valid JSON in this exact format.

# {{
#   "classification": {{
#     "category": "",
#     "urgency": "",
#     "reason": ""
#   }},
#   "plan": {{
#     "department": "",
#     "priority": "",
#     "actions": []
#   }},
#   "routing": {{
#     "assigned_team": "",
#     "ticket_status": "",
#     "estimated_resolution": "",
#     "next_step": ""
#   }},
#   "response": {{
#     "subject": "",
#     "customer_message": ""
#   }}
# }}
# """

#     response = ask_gemini(prompt)
#     return parse_json(response)