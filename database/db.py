import sqlite3


def create_database():
    conn = sqlite3.connect("workflow.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS workflow_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        request TEXT,
        category TEXT,
        urgency TEXT,
        department TEXT,
        assigned_team TEXT,
        ticket_status TEXT,
        subject TEXT,
        customer_message TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def log_workflow(
    request,
    classification,
    plan,
    routing,
    response
):
    conn = sqlite3.connect("workflow.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO workflow_logs (
        request,
        category,
        urgency,
        department,
        assigned_team,
        ticket_status,
        subject,
        customer_message
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        request,
        classification.get("category", ""),
        classification.get("urgency", ""),
        plan.get("department", ""),
        routing.get("assigned_team", ""),
        routing.get("ticket_status", ""),
        response.get("subject", ""),
        response.get("customer_message", "")
    ))

    conn.commit()
    conn.close()