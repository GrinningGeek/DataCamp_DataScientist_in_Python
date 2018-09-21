'''
A t-SNE map of the stock market

t-SNE provides great visualizations when the individual samples can be labeled. 
In this exercise, you'll apply t-SNE to the company stock price data. A scatter 
plot of the resulting t-SNE features, labeled by the company names, gives you a 
map of the stock market! The stock price movements for each company are available 
as the array normalized_movements (these have already been normalized for you). 
The list companies gives the name of each company. PyPlot (plt) has been 
imported for you.

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Import TSNE from sklearn.manifold.
Create a TSNE instance called model with learning_rate=50.
Apply the .fit_transform() method of model to normalized_movements. Assign the 
result to tsne_features.
Select column 0 and column 1 of tsne_features.
Make a scatter plot of the t-SNE features xs and ys. Specify the additional 
keyword argument alpha=0.5.
Code to label each point with its company name has been written for you using 
plt.annotate(), so just hit 'Submit Answer' to see the visualization!
'''
#Done by DataCamp
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

movements = pd.read_csv('E:/DataCamp/Unsupervised-learning-in-python/data/company-stock-movements-2010-2015-incl.csv')

companies = movements.iloc[:,0].unique().tolist()

movements = movements.drop(movements.columns[0], axis = 1)

movements = movements.values

import numpy as np
from sklearn.preprocessing import normalize

X = np.asarray(movements, dtype=np.float)

#One way to normalize the vector is to apply l2-normalization to scale the 
#vector to have a unit norm. “Unit norm” essentially means that if we squared 
#each element in the vector, and summed them, it would equal 1.
normalized_movements = normalize(X, norm='l2')

#Original values
# Create a TSNE instance: model
model = TSNE(learning_rate=50, random_state=18)

# Apply fit_transform to normalized_movements: tsne_features
tsne_features = model.fit_transform(movements)

# Select the 0th feature: xs
xs = tsne_features[:,0]

# Select the 1th feature: ys
ys = tsne_features[:,1]

# Scatter plot
plt.scatter(xs, ys, alpha=0.5)

# Annotate the points
for x, y, company in zip(xs, ys, companies):
    plt.annotate(company, (x, y), fontsize=5, alpha=0.75) 
#End done by DataCamp


# Import TSNE
from sklearn.manifold import TSNE

# Create a TSNE instance: model
model = TSNE(learning_rate=50, random_state=18)

# Apply fit_transform to normalized_movements: tsne_features
tsne_features = model.fit_transform(normalized_movements)

# Select the 0th feature: xs
xs = tsne_features[:,0]

# Select the 1th feature: ys
ys = tsne_features[:,1]

# Scatter plot
plt.scatter(xs, ys, alpha=0.5)

# Annotate the points
for x, y, company in zip(xs, ys, companies):
    plt.annotate(company, (x, y), fontsize=5, alpha=0.75)
plt.show()
