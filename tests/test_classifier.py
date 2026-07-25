from agents.classifier import classify_request

request = "I paid twice for my order and still haven't received a refund."
result = classify_request(request)
print(result)