import pandas as pd

df = pd.read_csv(r"D:\DS-Lab\dataset\Titanic-Dataset.csv")

print("First 5 rows of input CSV:")
print(df.head())

print("\nShape of dataset (rows, columns):")
print(df.shape)

df["new_column"] = "Sample"

output_file = r"D:\DS-Lab\ex1a_readAndWriteCSV\output.csv"
df.to_csv(output_file, index = False)

print("\nData successfully read from input_data.csv")
print("Data successfully written to output_data.csv")
print("\n")
