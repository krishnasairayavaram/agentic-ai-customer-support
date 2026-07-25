from agents.planner import plan_actions
from agents.classifier import classify_request

request="I paid twice for my order and still haven't received a refund."
classification=classify_request(request)
plan=plan_actions(classification)

print("Classification:")
print(classification)

print("\nExecution Plan:")
print(plan)