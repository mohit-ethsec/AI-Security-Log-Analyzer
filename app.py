from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def dashboard():

    with open("reports/security_report.json", "r") as report:
        data = json.load(report)

    total_ips = len(data)

    high_risk = sum(1 for item in data if item["risk"] == "HIGH")
    medium_risk = sum(1 for item in data if item["risk"] == "MEDIUM")
    low_risk = sum(1 for item in data if item["risk"] == "LOW")

    return render_template(
        "dashboard.html",
        data=data,
        total_ips=total_ips,
        high_risk=high_risk,
        medium_risk=medium_risk,
        low_risk=low_risk
    )

if __name__ == "__main__":
    app.run(debug=True)
