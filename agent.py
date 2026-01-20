from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from tools.case_tools import find_existing_case, create_new_case
from tools.alert_tools import create_alert
from tools.merge_tools import merge_alert_into_case
from prompts import SYSTEM_PROMPT
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

agent = initialize_agent(
    tools=[
        find_existing_case,
        create_new_case,
        create_alert,
        merge_alert_into_case
    ],
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    system_message=SYSTEM_PROMPT,
    verbose=True
)

def run_soar_agent(alert):
    return agent.run(
        f"""
        Automate SOAR for this Wazuh alert:

        {alert}
        """
    )

