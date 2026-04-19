# import pandas as pd
# import numpy as np
# from scipy import stats

# # ---------------------------------------------------
# # Read Titanic dataset
# # ---------------------------------------------------
# file_path = r"D:\DS-Lab\dataset\Titanic-Dataset.csv"
# df = pd.read_csv(file_path)

# # ---------------------------------------------------
# # One-Sample t-test
# # Test whether mean Age differs from a population mean (example: 30)
# # ---------------------------------------------------
# age_data = df["Age"].dropna()   # remove missing ages
# mu = 30                          # population mean

# t_statistic_1samp, p_value_1samp = stats.ttest_1samp(age_data, mu)

# print("One-Sample t-test (Age vs population mean 30)")
# print("t-statistic:", t_statistic_1samp)
# print("p-value:", p_value_1samp)
# print()

# # ---------------------------------------------------
# # Independent Two-Sample t-test
# # Compare Fare of Survived vs Not Survived passengers
# # ---------------------------------------------------
# group1 = df[df["Survived"] == 1]["Fare"].dropna()
# group2 = df[df["Survived"] == 0]["Fare"].dropna()

# t_statistic_ind, p_value_ind = stats.ttest_ind(group1, group2)

# print("Independent Two-Sample t-test (Fare: Survived vs Not Survived)")
# print("t-statistic:", t_statistic_ind)
# print("p-value:", p_value_ind)
# print()

# # ---------------------------------------------------
# # Paired Sample t-test
# # Compare a passenger’s original fare vs normalized fare
# # (same people → paired data)
# # ---------------------------------------------------
# fare = df["Fare"].dropna()
# fare_normalized = (fare - fare.mean()) / fare.std()  # simple normalization

# # Ensure equal sample size
# min_size = min(len(fare), len(fare_normalized))
# fare = fare.iloc[:min_size]
# fare_normalized = fare_normalized.iloc[:min_size]

# t_statistic_rel, p_value_rel = stats.ttest_rel(fare, fare_normalized)

# print("Paired Sample t-test (Fare vs Normalized Fare)")
# print("t-statistic:", t_statistic_rel)
# print("p-value:", p_value_rel)
# print("\n")

import numpy as np
from scipy import stats

# One-Sample t-test
data = [102, 100, 98, 101, 99, 97, 100, 103, 98, 99]
mu = 100

t_statistic_1samp, p_value_1samp = stats.ttest_1samp(data, mu)

print("One-Sample t-test")
print("t-statistic:", t_statistic_1samp)
print("p-value:", p_value_1samp)
print()

# Independent Two-Sample t-test
group1 = [102, 100, 98, 101, 99, 97, 100, 103, 98, 99]
group2 = [110, 108, 107, 109, 106, 105, 111, 107, 108, 109]

t_statistic_ind, p_value_ind = stats.ttest_ind(group1, group2)

print("Independent Two-Sample t-test")
print("t-statistic:", t_statistic_ind)
print("p-value:", p_value_ind)
print()

# Paired Sample t-test
before_treatment = [102, 100, 98, 101, 99, 97, 100, 103, 98, 99]
after_treatment = [105, 103, 101, 104, 102, 100, 104, 106, 101, 102]

t_statistic_rel, p_value_rel = stats.ttest_rel(before_treatment, after_treatment)

print("Paired Sample t-test")
print("t-statistic:", t_statistic_rel)
print("p-value:", p_value_rel)