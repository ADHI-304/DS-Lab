import pandas as pd
import numpy as np
from scipy import stats

def one_sample_z_test(sample_mean, population_mean, population_stddev, sample_size):
    standard_error = population_stddev / np.sqrt(sample_size)
    z_score = (sample_mean - population_mean) / standard_error
    p_value = stats.norm.cdf(z_score)
    return z_score, p_value

file_path = r"C:\DS__lab\dataset\Titanic-Dataset.csv"
df = pd.read_csv(file_path)

age_data = df["Age"].dropna()

sample_mean = age_data.mean()
sample_size = age_data.count()
population_mean = float(input("Enter the population mean for Age: "))
population_stddev = float(input("Enter the population std deviation for Age: "))

z_score, p_value = one_sample_z_test(sample_mean, population_mean,
                                     population_stddev, sample_size)


print("\nSample Mean (Age):", sample_mean)
print("Sample Size:", sample_size)
print("Z-score:", z_score)
print("P-value:", p_value)
