import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ---------------------------------------------------
# Load Titanic dataset
# ---------------------------------------------------
file_path = r"C:\DS__lab\dataset\Titanic-Dataset.csv"
df = pd.read_csv(file_path)

# Select useful features and drop missing values
df = df[['Age', 'Fare', 'Survived']].dropna()

# ---------------------------------------------------
# Define features (X) and target (y)
# ---------------------------------------------------
X = df[['Age', 'Fare']]   # Features
y = df['Survived']         # Target

# ---------------------------------------------------
# Split the dataset into training and testing sets
# ---------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------------------------------
# Create Logistic Regression model
# ---------------------------------------------------
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# ---------------------------------------------------
# Make predictions
# ---------------------------------------------------
y_pred = model.predict(X_test)

# ---------------------------------------------------
# Evaluate the model
# ---------------------------------------------------
print("\n")
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred, labels=[0, 1])
class_report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
print("\n")
print(f"Classification Report:\n{class_report}")
