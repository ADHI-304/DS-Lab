import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------
# Load Titanic Dataset
# ---------------------------------------------------
file_path = r"C:\DS__lab\dataset\Titanic-Dataset.csv"
df = pd.read_csv(file_path)

# Select required numeric columns and drop missing values
df = df[['Fare', 'Age', 'Pclass', 'SibSp', 'Parch']].dropna()

# ---------------------------------------------------
# Define features (X) and target variable (y)
# Predict Fare using multiple features
# ---------------------------------------------------
X = df[['Age', 'Pclass', 'SibSp', 'Parch']]
y = df['Fare']

# Add constant term for intercept
X = sm.add_constant(X)

# ---------------------------------------------------
# Fit the Multiple Linear Regression model
# ---------------------------------------------------
model = sm.OLS(y, X).fit()

# ---------------------------------------------------
# Actual vs Predicted Plot
# ---------------------------------------------------
plt.figure(figsize=(10, 6))
plt.scatter(y, model.predict(X), color='blue')
plt.plot(y, y, color='red')   # perfect prediction diagonal
plt.title('Actual vs Predicted')
plt.xlabel('Actual Fare')
plt.ylabel('Predicted Fare')
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Residual Plots
# ---------------------------------------------------
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# 1. Residuals vs Fitted
sns.residplot(x=model.fittedvalues, y=model.resid, lowess=True,
              line_kws={'color': 'red'}, ax=axs[0])
axs[0].set_title('Residuals vs Fitted')
axs[0].set_xlabel('Fitted values')
axs[0].set_ylabel('Residuals')

# 2. Normal Q-Q plot
sm.qqplot(model.resid, line='s', ax=axs[1])
axs[1].set_title('Normal Q-Q')
axs[1].set_xlabel('Theoretical Quantiles')
axs[1].set_ylabel('Sample Quantiles')

# 3. Scale-Location plot
sns.regplot(x=model.fittedvalues, y=np.sqrt(np.abs(model.resid)), lowess=True,
            line_kws={'color': 'red'}, ax=axs[2])
axs[2].set_title('Scale-Location')
axs[2].set_xlabel('Fitted values')
axs[2].set_ylabel('sqrt(abs(Residuals))')

plt.tight_layout()
plt.show()

# ---------------------------------------------------
# Print the Regression Summary
# ---------------------------------------------------
print(model.summary())
