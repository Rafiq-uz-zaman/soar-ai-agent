def normalize_wazuh_alert(raw):
    rule = raw.get("rule", {})
    agent = raw.get("agent", {})

    return {
        "rule_id": rule.get("id"),
        "rule_level": rule.get("level"),
        "rule_description": rule.get("description"),

        "agent_name": agent.get("name"),
        "agent_ip": agent.get("ip"),

        "full_log": raw.get("full_log"),
        "timestamp": raw.get("timestamp"),

        "alert_type": raw.get("alert_type"),
        "severity": raw.get("severity"),

        "iris": {
            "case_title": raw.get("iris_case_title"),
            "template_id": raw.get("iris_case_template_id"),
            "customer_id": raw.get("iris_customer_id"),
            "tags": raw.get("iris_alert_tags"),
            "case_behavior": raw.get("iris_cases"),
            "alert_severity_id": raw.get("iris_alert_severity_id"),
            "alert_status_id": raw.get("iris_alert_status_id"),
            "description": raw.get("iris_description"),
        }
    }
