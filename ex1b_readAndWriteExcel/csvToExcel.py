import pandas as pd

input_file = r"C:\DS__lab\dataset\Titanic-Dataset.csv"
df = pd.read_csv(input_file)

df.to_excel("Titanic-Dataset.xlsx", index=False)

print("CSV successfully converted to Excel")
