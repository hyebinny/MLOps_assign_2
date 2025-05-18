# Apply AutoML to the problem in assignment-1

import pandas as pd
from supervised.automl import AutoML
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the preprocessed dataset
csv_path = os.path.expanduser("~/assign-2/data/preprocessed.csv")
df = pd.read_csv(csv_path)

# Split into features and label
X = df.drop(columns=["target"])
y = df["target"]

# Train / Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=42
)

# AutoML configuration
automl = AutoML(
        results_path = "AutoML_Results_explain",
        mode = "Explain",
        total_time_limit = 300,
        explain_level = 2
        )

# Run AutoML process
automl.fit(X_train, y_train)

# Predict wiht the best model
predictions = automl.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))
