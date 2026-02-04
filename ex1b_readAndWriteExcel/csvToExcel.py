import pandas as pd

df = pd.read_csv(r"C:\DS__lab\dataset\Titanic-Dataset.csv")

df.to_excel("Titanic-Dataset.xlsx", index=False)

print("CSV successfully converted to Excel")
