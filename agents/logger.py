from database.db import log_workflow

def save_workflow(request, classification, plan, routing,response):
    log_workflow(request, classification, plan, routing, response)