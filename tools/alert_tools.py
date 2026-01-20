from langchain_core.tools import tool
from iris_client import IRISIntegration
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("IRIS_API_KEY")
base_url = os.getenv("IRIS_URL")

iris = IRISIntegration(
    api_key="YOUR_IRIS_API_KEY",
    base_url="YOUR_IRIS_URL"
)

@tool
def create_alert(alert_payload: dict):
    """Create IRIS alert"""
    return iris.create_alert(alert_payload)


