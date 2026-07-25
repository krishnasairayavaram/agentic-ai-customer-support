from agents.classifier import classify_request
from agents.planner import plan_actions
from agents.router import route_request

request = "I paid twice for my order and still haven't received a refund."
classification=classify_request(request)
plan=plan_actions(classification)
routing=route_request(plan)

print("Classification")
print(classification)

print("\nPlan")
print(plan)

print("\nRouting")
print(routing)