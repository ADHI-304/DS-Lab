import pandas as pd

input_file = r"C:\DS__lab\ex1b_readAndWriteExcel\Titanic-Dataset.xlsx"   
df = pd.read_excel(input_file)

print("First 5 rows of input Excel file:")
print(df.head())

print("\nShape of dataset (rows, columns):")
print(df.shape)

df["new_column"] = "Sample"

output_file = r"C:\DS__lab\ex1b_readAndWriteExcel\Titanic-Dataset-new.xlsx"
df.to_excel(output_file, index=False)

print("\nData successfully read from Titanic-Dataset.xlsx")
print("Data successfully written to Titanic-Dataset1.xlsx")
