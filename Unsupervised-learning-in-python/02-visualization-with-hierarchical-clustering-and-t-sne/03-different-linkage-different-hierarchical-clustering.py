'''
Different linkage, different hierarchical clustering!

In the video, you saw a hierarchical clustering of the voting countries at the 
Eurovision song contest using 'complete' linkage. Now, perform a hierarchical 
clustering of the voting countries with 'single' linkage, and compare the 
resulting dendrogram with the one in the video. Different linkage, 
different hierarchical clustering!

You are given an array samples. Each row corresponds to a voting country, and 
each column corresponds to a performance that was voted for. The list 
country_names gives the name of each voting country. This dataset was obtained 
from Eurovision.

INSTRUCTIONS
100XP
INSTRUCTIONS
100XP
Import:
linkage and dendrogram from scipy.cluster.hierarchy.
matplotlib.pyplot as plt.
Perform hierarchical clustering on samples using the linkage() function with 
the method='single' keyword argument. Assign the result to mergings.
Plot a dendrogram of the hierarchical clustering, using the list country_names 
as the labels. In addition, specify the leaf_rotation=90, and leaf_font_size=6 
keyword arguments as you have done earlier.
'''
#Done by DataCamp
import pandas as pd
from numpy import genfromtxt

country_names = pd.read_csv('E:/DataCamp/Unsupervised-learning-in-python/data/eurovision-2016.csv')

country_names = country_names.iloc[:,0].unique().tolist()

samples = genfromtxt('E:/DataCamp/Unsupervised-learning-in-python/data/eurovision_votes.csv', delimiter=',')

#End done by DataCamp

# Perform the necessary imports
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

# Calculate the linkage: mergings
mergings = linkage(samples, method='single')

# Plot the dendrogram
dendrogram(mergings, labels=country_names, leaf_rotation=90, leaf_font_size=6)
plt.show()
