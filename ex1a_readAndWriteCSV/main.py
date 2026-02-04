import pandas as pd

input_file = r"C:\DS__lab\dataset\Titanic-Dataset.csv"     
df = pd.read_csv(input_file)

print("First 5 rows of input CSV:")
print(df.head())

print("\nShape of dataset (rows, columns):")
print(df.shape)

df["new_column"] = "Sample"

output_file = r"C:\DS__lab\ex1a_readAndWriteCSV\Titanic-Dataset-new.csv"
df.to_csv(output_file, index=False)

print("\nData successfully read from input_data.csv")
print("Data successfully written to output_data.csv")
print("\n")
