import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)
st.header("🏗 System Architecture")

st.image("architecture.png", use_container_width=True)
st.title("ℹ️ About This Project")

st.markdown("""
## 🤖 AI Customer Support Workflow

This project demonstrates an **Agentic AI Customer Support Workflow** that automatically processes customer requests using multiple AI agents.

The system classifies customer requests, creates an execution plan, routes the request to the appropriate support team, generates a professional customer response, and stores the complete workflow in a SQLite database.

This project was developed as part of the **AI & Analytics Proof of Concept (POC)**.
""")

st.divider()

# ------------------------------------------------------
# Technology Stack
# ------------------------------------------------------

st.header("🛠 Technology Stack")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
### Frontend
- Streamlit

### Backend
- Python

### AI Model
- Google Gemini 3.5 Flash
""")

with col2:

    st.markdown("""
### Database
- SQLite

### Libraries
- google-genai
- pandas
- python-dotenv
""")

st.divider()

# ------------------------------------------------------
# Workflow
# ------------------------------------------------------

st.header("🔄 Multi-Agent Workflow")

st.code("""
Customer Request
        │
        ▼
Classifier Agent
        │
        ▼
Planner Agent
        │
        ▼
Router Agent
        │
        ▼
Response Agent
        │
        ▼
Logger Agent
        │
        ▼
SQLite Database
""")

st.divider()

# ------------------------------------------------------
# AI Agents
# ------------------------------------------------------

st.header("🤖 AI Agents")

agents = [
    ("Classifier Agent",
     "Classifies the customer request into Complaint, Service Request, General Enquiry or Escalation and determines urgency."),

    ("Planner Agent",
     "Creates an execution plan including department assignment, priority and action items."),

    ("Router Agent",
     "Routes the request to the appropriate support team and estimates resolution time."),

    ("Response Agent",
     "Generates a professional and empathetic customer response."),

    ("Logger Agent",
     "Stores the complete workflow into the SQLite database for future reference.")
]

for title, description in agents:

    with st.container(border=True):
        st.subheader(title)
        st.write(description)

st.divider()

# ------------------------------------------------------
# Features
# ------------------------------------------------------

st.header("✨ Features")

st.markdown("""
- ✅ Multi-Agent AI Workflow
- ✅ Customer Request Classification
- ✅ Intelligent Execution Planning
- ✅ AI-based Request Routing
- ✅ Automated Customer Response Generation
- ✅ Workflow Logging using SQLite
- ✅ Workflow History Dashboard
- ✅ CSV Export of Workflow History
- ✅ Professional Streamlit Dashboard
""")

st.divider()

# ------------------------------------------------------
# Project Architecture
# ------------------------------------------------------

st.header("🏗 Project Structure")

st.code("""
firstsource/
│
├── app.py
│
├── agents/
│   ├── classifier.py
│   ├── planner.py
│   ├── router.py
│   ├── responder.py
│   └── logger.py
│
├── database/
│   └── db.py
│
├── pages/
│   ├── Workflow_History.py
│   └── About.py
│
├── utils/
│   ├── gemini_client.py
│   └── json_parser.py
│
├── workflow.db
├── requirements.txt
└── README.md
""")

st.divider()

# ------------------------------------------------------
# Developer
# ------------------------------------------------------

st.header("👨‍💻 Developer")

st.success("""
**Developer:** Krishna Sai

**Project:** AI Customer Support Workflow

**Architecture:** Multi-Agent AI

**LLM:** Google Gemini 3.5 Flash

**Database:** SQLite
""")

st.caption("© 2026 AI Customer Support Workflow")