import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# ---------------------------------------------------
# Step 1: Load Titanic Dataset
# ---------------------------------------------------
file_path = r"C:\DS__lab\dataset\Titanic-Dataset.csv"
df = pd.read_csv(file_path)

# Select required numeric columns
df = df[['Age', 'Fare']].dropna()

# ---------------------------------------------------
# Step 2: Define features (X) and target (y)
# Predict Fare using Age
# ---------------------------------------------------
X = df[['Age']]     # Feature
y = df['Fare']      # Target

# ---------------------------------------------------
# Step 3: Split data
# ---------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------------------------------
# Step 4: Create and train the Linear Regression model
# ---------------------------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# ---------------------------------------------------
# Step 5: Make predictions on test data
# ---------------------------------------------------
y_pred = model.predict(X_test)

# ---------------------------------------------------
# Step 6: Evaluate the model
# ---------------------------------------------------
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n")
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# ---------------------------------------------------
# Step 7: Visualize the results
# ---------------------------------------------------
plt.scatter(X_test, y_test, color='black', label='Actual')
plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Predicted')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Linear Regression: Predicting Titanic Fare using Age')
plt.legend()
plt.show()

# ---------------------------------------------------
# Step 8: Predict Fare for a new Age (Example: Age = 40)
# ---------------------------------------------------
new_age = pd.DataFrame({'Age': [40]})
predicted_fare = model.predict(new_age)

print(f"Predicted Fare for a passenger aged 40: ${predicted_fare[0]:.2f}")
print("\n")
