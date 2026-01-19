from langchain_core.tools import tool
from iris_client import IRISIntegration

iris = IRISIntegration(
    api_key="YOUR_IRIS_API_KEY",
    base_url="https://192.168.18.122"
)

@tool
def merge_alert_into_case(alert_id: int, case_id: int):
    """Merge alert into case"""
    return iris.merge_alert(alert_id, case_id)
