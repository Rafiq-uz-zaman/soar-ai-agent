import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("IRIS_API_KEY")
base_url = os.getenv("IRIS_URL")

requests.packages.urllib3.disable_warnings()

class IRISIntegration:
    def __init__(self, api_key, base_url):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def _request(self, method, endpoint, **kwargs):
        kwargs.setdefault("verify", False)
        kwargs["headers"] = self.headers
        res = requests.request(method, f"{self.base_url}{endpoint}", **kwargs)
        if res.status_code in [200, 201]:
            return res.json().get("data")
        raise Exception(res.text)

    def find_case(self, title, customer_id):
        data = self._request("GET", f"/manage/cases/filter?case_name={title}")
        for c in data.get("cases", []):
            if c.get("client", {}).get("customer_id") == customer_id:
                return c.get("case_id")
        return None

    def create_case(self, payload):
        return self._request("POST", "/manage/cases/add", json=payload)

    def create_alert(self, payload):
        return self._request("POST", "/alerts/add", json=payload)

    def merge_alert(self, alert_id, case_id):
        return self._request(
            "POST",
            f"/alerts/merge/{alert_id}",
            json={
                "target_case_id": case_id,
                "note": "Merged by AI SOAR Agent",
                "import_as_event": False
            }
        )

