import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.metrics import confusion_matrix
import pandas as pd

# Generate synthetic classification data
X, y = make_classification(
    n_samples=200,
    n_features=2,
    n_informative=2,  # Informative features <= n_features
    n_redundant=0,    # No redundant features
    random_state=42
)

# Simulate predictions for illustration
y_pred = [1 if xi[0] + xi[1] > 0 else 0 for xi in X]

# Compute confusion matrix
cm = confusion_matrix(y, y_pred)

# Create a heatmap of the confusion matrix
sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=["Negative", "Positive"],
    yticklabels=["Negative", "Positive"]
)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix Heatmap")
plt.show()
