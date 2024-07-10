#EDA and linear regression 

import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LinearRegression

os.chdir("C:/Users/Khushi/OneDrive/Desktop/data+codes/datasets")
mtcars = pd.read_csv('CarPrice_Assignment.csv')

print(mtcars.head())
print(mtcars.describe())

# Exploratory Data Analysis (EDA) with visualizations
# Pairplot to visualize relationships between all numerical variables
sns.pairplot(mtcars)
#sns.pairplot(mtcars.drop(['car_ID'],axis=1),height=3)

# Countplot for categorical variable 'enginetype'
sns.countplot(x='enginetype', data=mtcars)

# Scatterplots of selected variables against 'price'
sns.scatterplot(x='horsepower', y='price', data=mtcars)
sns.scatterplot(x='compressionratio', y='price', data=mtcars)
sns.scatterplot(x='enginesize', y='price', data=mtcars)
sns.scatterplot(x='cylindernumber', y='price', data=mtcars)
sns.scatterplot(x='enginetype', y='price', data=mtcars)
sns.scatterplot(x='carheight', y='price', data=mtcars)
sns.scatterplot(x='carwidth', y='price', data=mtcars)
sns.scatterplot(x='carlength', y='price', data=mtcars)
sns.scatterplot(x='wheelbase', y='price', data=mtcars)
sns.scatterplot(x='fueltype', y='price', data=mtcars)

# Boxplot of 'price' to visualize distribution and outliers
sns.boxplot(y='price', data=mtcars)
# Boxplot of 'price' grouped by 'enginetype'
sns.boxplot(x='enginetype', y='price', data=mtcars)
# Boxplot of 'compressionratio' grouped by 'fueltype'
sns.boxplot(x='fueltype', y='compressionratio',data=mtcars)

# Uncomment the next line to display plots if using Matplotlib
# plt.show()


# Single variable regression (Highway MPG vs Price)
x = mtcars[['highwaympg']] #independent variable
y = mtcars[['price']] # dependent variable
reg_single = LinearRegression()
# reg_single = linear_model.LinearRegression()
reg_single.fit(x, y)
#reg.fit([[0,0],[1,1],[2,2],[0,1,2]])

print("\nCoefficients for single variable regression (Highway MPG vs Price): ")
print(reg_single.coef_)

## Visualizing the relationship between Highway MPG and Price
sns.regplot(x=x['highwaympg'], y=y['price'])
plt.xlabel('Highway MPG')
plt.ylabel('Price')
plt.title('Regression plot: Highway MPG vs Price')
plt.show()

# Coefficient: -809.27352829 (inverse relation) -> Output Interpretation: as the fuel efficiency (highwaympg) increases, the price of the car decreases by approximately 809.27352829 units.
# It seems counterintuitive at first, but if we think about it,  the fuel-efficient cars are designed to be economical, targetting the budget-conscious consumers. Luxury cars on the other hand tend to be less fuel-efficient and are priced higher.


# Multiple regression (Price vs Horsepower and Curb Weight)
X = mtcars[['horsepower', 'curbweight']] # independent variables
Y = mtcars[['price']] # dependent
reg_multiple = LinearRegression()
#reg=linear_model.LinearRegression()
reg_multiple.fit(X, Y)
print("\nCoefficients for multiple regression (Price vs Horsepower and Curb Weight):")
print(reg_multiple.coef_)

# Coefficients for ['horsepower', 'curbweight'] -> [83.81225563, 8.03749183]
# Interpretation: As the horsepower & curbweight increases, the car price increases by those many units respectively
