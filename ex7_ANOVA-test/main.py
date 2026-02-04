import pandas as pd
import numpy as np
from scipy import stats

# ---------------------------------------------------
# Read the Titanic dataset
# ---------------------------------------------------
file_path = r"C:\DS__lab\dataset\Titanic-Dataset.csv"
df = pd.read_csv(file_path)

# Remove missing values in Fare and Pclass
df = df[["Fare", "Pclass"]].dropna()

# ---------------------------------------------------
# Create 3 groups based on Passenger Class
# ---------------------------------------------------
group1 = df[df["Pclass"] == 1]["Fare"]
group2 = df[df["Pclass"] == 2]["Fare"]
group3 = df[df["Pclass"] == 3]["Fare"]

# ---------------------------------------------------
# Perform the ANOVA test
# ---------------------------------------------------
f_statistic, p_value = stats.f_oneway(group1, group2, group3)
print("\n")
print(f"F-statistic: {f_statistic}")
print(f"p-value: {p_value}")

# ---------------------------------------------------
# Interpretation of the p-value
# ---------------------------------------------------
alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference between the group means.")
else:
    print("Fail to reject the null hypothesis: No significant difference between the group means.")
print("\n")