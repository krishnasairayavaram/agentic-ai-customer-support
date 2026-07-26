import sqlite3
import pandas as pd
import streamlit as st
from database.db import create_database

create_database()
st.set_page_config(
    page_title="Workflow History",
    page_icon="📜",
    layout="wide"
)

st.title("📜 Workflow History")

st.write("View all AI workflow requests processed by the system.")

conn = sqlite3.connect("workflow.db")

query = """
SELECT
    id,
    request,
    category,
    urgency,
    department,
    assigned_team,
    ticket_status,
    subject,
    timestamp
FROM workflow_logs
ORDER BY id DESC
"""

df = pd.read_sql_query(query, conn)

conn.close()

if df.empty:

    st.info("No workflow records found.")

else:

    st.success(f"Total Requests Processed : {len(df)}")

    st.divider()

    category_filter = st.selectbox(
        "Filter by Category",
        ["All"] + sorted(df["category"].dropna().unique().tolist())
    )

    if category_filter != "All":
        df = df[df["category"] == category_filter]

    st.dataframe(
        df,
        width="stretch",
        hide_index=True
    )

    st.download_button(
        label="⬇ Download CSV",
        data=df.to_csv(index=False),
        file_name="workflow_history.csv",
        mime="text/csv"
    )