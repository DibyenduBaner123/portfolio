def trigger_alert(risk_score):
    if risk_score > 70:
        return "⚠️ Critical Alert: High Risk Project!"
    elif risk_score > 40:
        return "⚠️ Moderate Risk Warning"
    else:
        return "✅ Project Stable"