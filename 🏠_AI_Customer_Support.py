import json
import sqlite3
import time

import streamlit as st

from agents.classifier import classify_request
from agents.planner import plan_actions
from agents.router import route_request
from agents.responder import generate_response
from agents.logger import save_workflow

st.set_page_config(
    page_title="AI Customer Support Workflow",
    page_icon="🤖",
    layout="wide"
)

# ==================================================
# Dashboard Statistics
# ==================================================

conn = sqlite3.connect("workflow.db")
cursor = conn.cursor()

try:
    cursor.execute("SELECT COUNT(*) FROM workflow_logs")
    total_requests = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM workflow_logs WHERE category='Complaint'"
    )
    total_complaints = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM workflow_logs WHERE urgency='High'"
    )
    high_priority = cursor.fetchone()[0]

except Exception:
    total_requests = 0
    total_complaints = 0
    high_priority = 0

conn.close()

# ==================================================
# Sidebar
# ==================================================

with st.sidebar:

    st.title("🤖 AI Customer Support")

    st.markdown("---")

    st.subheader("📊 Dashboard")

    st.metric("Total Requests", total_requests)
    st.metric("Complaints", total_complaints)
    st.metric("High Priority", high_priority)

    st.markdown("---")

    st.subheader("📌 Project Information")

    st.write("**Assignment:** AI & Analytics POC")
    st.write("**Architecture:** Multi-Agent AI")
    st.write("**LLM:** Gemini 3.5 Flash")
    st.write("**Database:** SQLite")

    st.markdown("---")

    st.subheader("👨‍💻 Developer")

    st.write("Krishna Sai")

    st.markdown("---")

    st.success("✔ Multi-Agent AI")
    st.success("✔ SQLite Logging")
    st.success("✔ Workflow History")
    st.success("✔ AI Generated Response")

# ==================================================
# Header
# ==================================================

st.title("🤖 AI Customer Support Workflow")

st.write(
    "Enter a customer request below and click **Process Request**."
)

request = st.text_area(
    "Customer Request",
    height=180,
    placeholder="Example: I paid twice for my order and still haven't received my refund."
)

# ==================================================
# Process Request
# ==================================================

if st.button("🚀 Process Request", use_container_width=True):

    if not request.strip():

        st.warning("Please enter a customer request.")

    else:

        start_time = time.time()

        with st.spinner("Processing request..."):

            classification = classify_request(request)

            plan = plan_actions(classification)

            routing = route_request(plan)

            reply = generate_response(
                request,
                classification,
                plan,
                routing
            )

            save_workflow(
                request,
                classification,
                plan,
                routing,
                reply
            )

        end_time = time.time()

        processing_time = round(end_time - start_time, 2)

        st.success("✅ Workflow completed successfully!")

        st.caption(f"⏱ Processing Time: {processing_time} seconds")

        st.divider()

        # ==================================================
        # Classification
        # ==================================================

        st.subheader("📋 Classification")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Category",
                classification.get("category", "N/A")
            )

        with col2:
            st.metric(
                "Urgency",
                classification.get("urgency", "N/A")
            )

        st.info(classification.get("reason", "N/A"))

        # ==================================================
        # Execution Plan
        # ==================================================

        st.divider()

        st.subheader("📝 Execution Plan")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Department",
                plan.get("department", "N/A")
            )

        with col2:
            st.metric(
                "Priority",
                plan.get("priority", "N/A")
            )

        st.markdown("### 📌 Actions")

        actions = plan.get("actions", [])

        if actions:
            for i, action in enumerate(actions, start=1):
                st.write(f"✅ {i}. {action}")
        else:
            st.write("No actions available.")

        # ==================================================
        # Routing
        # ==================================================

        st.divider()

        st.subheader("🚦 Routing")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Assigned Team",
                routing.get("assigned_team", "N/A")
            )

            st.metric(
                "Ticket Status",
                routing.get("ticket_status", "N/A")
            )

        with col2:
            st.metric(
                "Estimated Resolution",
                routing.get("estimated_resolution", "N/A")
            )

        st.success(
            f"**Next Step:** {routing.get('next_step', 'N/A')}"
        )

        # ==================================================
        # Customer Response
        # ==================================================

        st.divider()

        st.subheader("💬 Customer Response")

        st.markdown(f"### {reply.get('subject', 'N/A')}")

        with st.container(border=True):

            st.write(
                reply.get(
                    "customer_message",
                    "No response generated."
                )
            )

        # ==================================================
        # Download Report
        # ==================================================

        st.divider()

        report = {
            "classification": classification,
            "plan": plan,
            "routing": routing,
            "response": reply
        }

        st.download_button(
            label="⬇ Download Workflow Report (JSON)",
            data=json.dumps(report, indent=4),
            file_name="workflow_report.json",
            mime="application/json"
        )

        # ==================================================
        # Raw JSON
        # ==================================================

        with st.expander("🔍 View Raw JSON"):

            st.write("### Classification")
            st.json(classification)

            st.write("### Execution Plan")
            st.json(plan)

            st.write("### Routing")
            st.json(routing)

            st.write("### Customer Response")
            st.json(reply)
            
st.divider()

st.caption(
    "AI Customer Support Workflow | Multi-Agent AI | Powered by Google Gemini 3.5 Flash"
)