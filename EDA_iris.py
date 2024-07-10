# Basic EDA, plots, using inbuilt iris dataset
import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

# Set the working directory (replace "path" with your actual path)
os.chdir("C:/Users/Khushi/OneDrive/Desktop/data+codes/datasets")

# Load the dataset
iris = pd.read_csv('Iris.csv')

# Display the first few rows and basic statistics of the dataset
print(iris.head())
print(iris.describe())

# Count plot of species
sns.countplot(x='Species', data=iris)
plt.show()

# Scatter plot of SepalLengthCm vs SepalWidthCm
sns.scatterplot(x='SepalLengthCm', y='SepalWidthCm', hue='Species', data=iris)
plt.show()

# Pair plot of the dataset excluding the 'Id' column
sns.pairplot(iris.drop(['Id'], axis=1), hue='Species', height=2)
plt.show()

# Exclude non-numeric columns for correlation matrix
numeric_columns = iris.drop(columns=['Id', 'Species'])

# Compute the correlation matrix
corr_matrix = numeric_columns.corr(method='pearson')
print(corr_matrix)

# Plot the heatmap of the correlation matrix
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()

# Box plot of SepalWidthCm grouped by Species
plt.figure()
sns.boxplot(x='Species', y='SepalWidthCm', data=iris)
plt.show()

# Uncomment if seaborn needs to be installed
# cd python3 bin
# python -m pip install seaborn
# pip install seaborn
# py -m pip install seaborn
