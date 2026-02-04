import pandas as pd

csv_file = r"C:\DS__lab\dataset\Titanic-Dataset.csv"
df = pd.read_csv(csv_file)

summary_stats = df.describe()

mean = df.mean(numeric_only=True)

median = df.median(numeric_only=True)

numeric_df = df.select_dtypes(include='number')

quartiles = numeric_df.quantile([0.25, 0.5, 0.75])

print("Summary Statistics:")
print(summary_stats)

print("\nMean:")
print(mean)

print("\nMedian:")
print(median)

print("\nQuartiles:")
print(quartiles)

print("\n")
