AI-Powered SOAR Agent (Wazuh → Shuffle → IRIS)

An AI-driven SOAR automation system that receives Wazuh alerts via webhook, uses a LangChain AI agent to decide actions, and automatically creates/merges cases and alerts in DFIR-IRIS.

This project replaces manual SOC workflows with LLM-based decision making + deterministic tools.


🚀 Features

✅ Receives Wazuh alerts via Shuffle webhook

🧠 AI agent (LangChain + OpenAI) acts as SOC analyst

🔧 Tool-based automation (safe & deterministic)

📂 Automatic case creation or merging

🚨 Automatic alert creation

🔗 Automatic alert-to-case merge

📋 Template-based IRIS cases

🏷 Intelligent tagging

🔍 Deduplication (rule + agent)

📈 Production-ready structure

⚡ Extensible to RAG, LangGraph, MITRE, etc.


🏗 Architecture

Wazuh
  ↓
Shuffle Webhook
  ↓
Flask API (/webhook/wazuh)
  ↓
Normalizer
  ↓
LangChain AI Agent
  ↓
IRIS Tools (API)
  ↓
DFIR-IRIS (Case + Alert)


⚙️ Requirements

Python 3.10+

OpenAI API key

DFIR-IRIS API access

Shuffle webhook

Wazuh alerts


📦 Installation
git clone https://github.com/your-org/soar-ai-agent.git
cd soar-ai-agent
pip install -r requirements.txt


🔑 Environment Setup

1️⃣ OpenAI API Key in .env file
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
IRIS_API_KEY=B8xxxxxxxxxxxx
IRIS_URL=httpsxxxxxxxxxxx

2️⃣ Update IRIS API credentials
tools/case_tools.py
tools/alert_tools.py
tools/merge_tools.py


api_key="YOUR_IRIS_API_KEY"
base_url="https://<IRIS-IP>"


▶️ Run the Server
python app.py


🌐 Webhook URL (Shuffle)

Configure Shuffle webhook to send Wazuh alerts to:
http://<SERVER-IP>:8000/webhook/wazuh
