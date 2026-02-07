📘 DS-Lab – Data Science Laboratory Exercises

This repository contains a collection of Data Science / Machine Learning lab exercises.
Each folder covers a core concept of data analysis using Python, Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn.

All exercises use the Titanic-Dataset.csv dataset located in the /dataset directory.

📂 Folder Structure
DS-Lab/
│
├── dataset/
│   └── Titanic-Dataset.csv
│
├── ex1a_readAndWriteCSV/
│   └── main.py       # Read CSV, write new CSV
│
├── ex1b_readAndWriteExcel/
│   └── main.py       # Read/write Excel files using pandas
│
├── ex2_descriptiveStatistics/
│   └── main.py       # Summary stats, mean, median, quartiles
│
├── ex3_visualization/
│   └── main.py       # Bar charts, histograms, scatter plots
│
├── ex4_correlationMatrix/
│   └── main.py       # Correlation heatmap and analysis
│
├── ex5_Z-test/
│   └── main.py       # Z-test implementation
│
├── ex6_T-test/
│   └── main.py       # One-sample & two-sample T-tests
│
├── ex7_ANOVA-test/
│   └── main.py       # ANOVA test for multiple groups
│
├── ex8_predictiveModelUsingLinearRegression/
│   └── main.py       # Linear regression model training & evaluation
│
├── ex9_predictiveModelUsingLogisticRegression/
│   └── main.py       # Logistic regression (Titanic Survival Prediction)
│
└── ex10_multipleRegression/
    └── main.py       # Multiple linear regression model

🚀 How to Run Each Exercise
1️⃣ Clone the Repository
git clone <repo-url>
cd DS-Lab

2️⃣ Create a Virtual Environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3️⃣ Install Required Packages
pip install -r requirements.txt

▶️ Running Any Exercise

Navigate into the exercise folder:

cd ex2_descriptiveStatistics
python main.py


If you get a path error, use relative paths like:

csv_file = "../dataset/Titanic-Dataset.csv"

📊 Overview of Concepts Covered
✅ Basic File Operations

Reading CSV files

Writing CSV/Excel files

Adding new columns

✅ Descriptive Statistics

Mean

Median

Quartiles

Summary Statistics (describe)

✅ Data Visualization

Histograms

Bar charts

Scatter plots

Correlation heatmaps

✅ Statistical Tests

Z-Test

T-Test

ANOVA

✅ Machine Learning Models

Linear Regression

Logistic Regression

Multiple Regression

Model evaluation metrics

🧪 Dataset

The repository uses a modified Titanic dataset with attributes needed for statistics and ML experiments.

Place your dataset here:

dataset/Titanic-Dataset.csv

🛠 Technologies Used

Python 3.12+

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

SciPy (for tests)

Virtualenv / Conda (optional)

👨‍💻 Author

Adhithyan R
DS/ML Lab Exercise Collection
Academic & Self-Learning Repository
