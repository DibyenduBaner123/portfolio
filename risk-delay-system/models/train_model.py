import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load data
data = pd.read_csv("data/sample_project_data.csv")

X = data.drop("risk", axis=1)
y = data["risk"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "models/risk_model.pkl")

print("Model Trained & Saved Successfully")