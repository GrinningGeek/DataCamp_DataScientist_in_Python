'''
Hierarchies of stocks

In chapter 1, you used k-means clustering to cluster companies according to 
their stock price movements. Now, you'll perform hierarchical clustering of the 
companies. You are given a NumPy array of price movements movements, where the 
rows correspond to companies, and a list of the company names companies. 
SciPy hierarchical clustering doesn't fit into a sklearn pipeline, so you'll 
need to use the normalize() function from sklearn.preprocessing instead of 
Normalizer.

linkage and dendrogram have already been imported from 
sklearn.cluster.hierarchy, and PyPlot has been imported as plt.

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Import normalize from sklearn.preprocessing.
Rescale the price movements for each stock by using the normalize() function on 
movements.
Apply the linkage() function to normalized_movements, using 'complete' linkage, 
to calculate the hierarchical clustering. Assign the result to mergings.
Plot a dendrogram of the hierarchical clustering, using the list companies of 
company names as the labels. In addition, specify the leaf_rotation=90, and 
leaf_font_size=6 keyword arguments as you did in the previous exercise.
'''
#Done by DataCamp
import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

movements = pd.read_csv('E:/DataCamp/Unsupervised-learning-in-python/data/company-stock-movements-2010-2015-incl.csv')

companies = movements.iloc[:,0].unique().tolist()

movements = movements.drop(movements.columns[0], axis = 1)

movements = movements.values

#End done by DataCamp

# Import normalize
from sklearn.preprocessing import normalize

# Normalize the movements: normalized_movements
normalized_movements = normalize(movements)

# Calculate the linkage: mergings
mergings = linkage(normalized_movements, method='complete')

# Plot the dendrogram
dendrogram(mergings, labels=companies, leaf_rotation=90, leaf_font_size=6)
plt.show()
