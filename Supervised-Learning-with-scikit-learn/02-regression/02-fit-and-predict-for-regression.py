'''
Fit & predict for regression

Now, you will fit a linear regression and predict life expectancy using just 
one feature. You saw Andy do this earlier using the 'RM' feature of the Boston 
housing dataset. In this exercise, you will use the 'fertility' feature of the 
Gapminder dataset. Since the goal is to predict life expectancy, the target 
variable here is 'life'. The array for the target variable has been pre-loaded 
as y and the array for 'fertility' has been pre-loaded as X_fertility.

A scatter plot with 'fertility' on the x-axis and 'life' on the y-axis has 
been generated. As you can see, there is a strongly negative correlation, so a 
linear regression should be able to capture this trend. Your job is to fit a 
linear regression and then predict the life expectancy, overlaying these 
predicted values on the plot to generate a regression line. You will also 
compute and print the R2 score using sckit-learn's .score() method.

INSTRUCTIONS
100XP
Import LinearRegression from sklearn.linear_model.
Create a LinearRegression regressor called reg.
Set up the prediction space to range from the minimum to the maximum of 
X_fertility. This has been done for you.
Fit the regressor to the data (X_fertility and y) and compute its predictions 
using the .predict() method and the prediction_space array.
Compute and print the R2 score using the .score() method.
Overlay the plot with your linear regression line. This has been done for you, so hit 'Submit Answer' to see the result!
'''
#Done by DataCamp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame: df
df = pd.read_csv('E:/DataCamp/Supervised-Learning-with-scikit-learn/data/gm_2008_region.csv')

# Create arrays for features and target variable
y = df['life'].values
X = df['fertility'].values

# Reshape X and y
y = y.reshape(-1,1)
X = X.reshape(-1,1)

X_fertility = df['fertility'].values
X_fertility = X_fertility.reshape(-1,1)

#End done by DataCamp

# Import LinearRegression
from sklearn.linear_model import LinearRegression

# Create the regressor: reg
reg = LinearRegression()

# Create the prediction space
prediction_space = np.linspace(min(X_fertility), max(X_fertility)).reshape(-1,1)

# Fit the model to the data
reg.fit(X_fertility, y)

# Compute predictions over the prediction space: y_pred
y_pred = reg.predict(prediction_space)

# Print R^2 
print(reg.score(X_fertility, y))

# Plot regression line
plt.scatter(df['fertility'], df['life'], color='blue')
plt.plot(prediction_space, y_pred, color='black', linewidth=3)
plt.xlabel('Fertility')
plt.ylabel('Life Expectancy')
plt.show()
