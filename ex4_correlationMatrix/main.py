import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = r"C:\DS__lab\dataset\Titanic-Dataset.csv"

df = pd.read_csv(file_path)

df_numeric = df.apply(pd.to_numeric, errors='coerce')

df_numeric = df_numeric.dropna(how='all')
df_numeric = df_numeric.dropna(axis=1, how='all')

if df_numeric.shape[0] < 2 or df_numeric.shape[1] < 2:
    print("Insufficient data to compute correlations after cleaning.")
else:
    correlation_matrix = df_numeric.corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    plt.title('Correlation Matrix for Titanic Dataset')
    plt.show()
