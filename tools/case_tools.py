from langchain_core.tools import tool
from iris_client import IRISIntegration

iris = IRISIntegration(
    api_key="YOUR_IRIS_API_KEY",
    base_url="YOUR_IRIS_URL"
)

@tool
def find_existing_case(title: str, customer_id: int):
    """Find existing IRIS case"""
    return iris.find_case(title, customer_id)

@tool
def create_new_case(case_payload: dict):
    """Create new IRIS case"""
    return iris.create_case(case_payload)

