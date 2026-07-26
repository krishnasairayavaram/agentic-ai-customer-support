import sqlite3

conn = sqlite3.connect("workflow.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM workflow_logs")

for row in cursor.fetchall():
    print("=" * 60)
    print(f"Request: {row[1]}")
    print(f"Category: {row[2]}")
    print(f"Urgency: {row[3]}")
    print(f"Department: {row[4]}")
    print(f"Assigned Team: {row[5]}")
    print(f"Status: {row[6]}")
    print(f"Subject: {row[7]}")
    print(f"Response:\n{row[8]}")
    print(f"Timestamp: {row[9]}")
conn.close()