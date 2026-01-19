from flask import Flask, request, jsonify
from agent import run_soar_agent
from normalizer import normalize_wazuh_alert

app = Flask(__name__)

@app.route("/webhook/wazuh", methods=["POST"])
def wazuh_webhook():
    raw_alert = request.json
    clean_alert = normalize_wazuh_alert(raw_alert)

    result = run_soar_agent(clean_alert)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
