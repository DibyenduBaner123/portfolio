import joblib
from services.preprocessing import preprocess_input

model = joblib.load("models/risk_model.pkl")

def calculate_risk(data_dict):
    processed = preprocess_input(data_dict)
    prediction = model.predict(processed)[0]
    probability = model.predict_proba(processed)[0][1]

    return {
        "risk_level": "High" if prediction == 1 else "Low",
        "risk_score": round(probability * 100, 2)
    }