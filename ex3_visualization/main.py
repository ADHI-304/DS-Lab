import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


np.random.seed(0)

data = pd.DataFrame({
    'A': np.random.normal(0, 1, 100),
    'B': np.random.normal(1, 2, 100),
    'C': np.random.normal(-1, 1.5, 100)
})

plt.figure(figsize=(10, 6))
sns.boxplot(data=data)

plt.scatter(data[data['A'] > 2].index,
            data[data['A'] > 2]['A'],
            color='red', label='Outliers in A')

plt.scatter(data[data['B'] > 4].index,
            data[data['B'] > 4]['B'],
            color='blue', label='Outliers in B')

plt.scatter(data[data['C'] < -2].index,
            data[data['C'] < -2]['C'],
            color='green', label='Outliers in C')

plt.title('Box Plot of Sample Data with Outliers')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='A', y='B', data=data, label='A vs B')
plt.scatter(data[data['A'] > 2]['A'],
            data[data['A'] > 2]['B'],
            color='red', label='Outliers')
plt.title('Scatter Plot of A vs B')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data['A'], kde=True, color='blue', bins=20)
plt.title('Histogram of Variable A')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
data.mean().plot(kind='bar', color='green')
plt.title('Mean of Variables')
plt.xlabel('Variables')
plt.ylabel('Mean')
plt.show()

plt.figure(figsize=(8, 8))
plt.pie(data.count(),
        labels=data.columns,
        autopct='%1.1f%%',
        startangle=140)
plt.title('Distribution of Variables')
plt.show()
