from flask import Flask, render_template, request
from services.risk_engine import calculate_risk
from services.alert_service import trigger_alert
from database.db import init_db, save_record, fetch_all_records

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def dashboard():
    result = None
    alert = None

    if request.method == "POST":
        data = {
            "completion_percent": float(request.form["completion"]),
            "budget_variance": float(request.form["budget"]),
            "resource_availability": float(request.form["resource"]),
            "delay_days": float(request.form["delay"]),
            "team_productivity": float(request.form["productivity"]),
            "complexity": float(request.form["complexity"])
        }

        result = calculate_risk(data)
        alert = trigger_alert(result["risk_score"])
        save_record(data, result)

    records = fetch_all_records()

    return render_template(
        "dashboard.html",
        result=result,
        alert=alert,
        records=records
    )

if __name__ == "__main__":
    app.run(debug=True, port=5003)