import pandas as pd

csv_file = r"D:\DS-Lab\dataset\Titanic-Dataset.csv"

excel_file = r"D:\DS-Lab\ex1b_readAndWriteExcel\Titanic-Dataset.xlsx"

df = pd.read_csv(csv_file)

df.to_excel(excel_file, index=False)

print("CSV successfully converted to Excel")