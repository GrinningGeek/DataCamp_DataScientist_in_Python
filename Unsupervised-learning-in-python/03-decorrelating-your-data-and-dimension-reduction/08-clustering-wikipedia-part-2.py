'''
Clustering Wikipedia part II

It is now time to put your pipeline from the previous exercise to work! You are
given an array articles of tf-idf word-frequencies of some popular Wikipedia 
articles, and a list titles of their titles. Use your pipeline to cluster the 
Wikipedia articles.

A solution to the previous exercise has been pre-loaded for you, so a Pipeline 
pipeline chaining TruncatedSVD with KMeans is available.

INSTRUCTIONS
100XP
Import pandas as pd.
Fit the pipeline to the word-frequency array articles.
Predict the cluster labels.
Align the cluster labels with the list titles of article titles by creating a 
DataFrame df with labels and titles as columns. This has been done for you.
Use the .sort_values() method of df to sort the DataFrame by the 'label' 
column, and print the result.
Hit 'Submit Answer' and take a moment to investigate your amazing clustering 
of Wikipedia pages!
'''
#Done by DataCamp
import pandas as pd
from scipy.sparse import csr_matrix

df = pd.read_csv('E:/DataCamp/Unsupervised-learning-in-python/data/Wikipedia_articles/wikipedia-vectors.csv', 
                 index_col=0)
articles = csr_matrix(df.transpose())
titles = list(df.columns)

#The reason for taking this transpose is that without it, there would be 
#13,000 columns (corresponding to the 13,000 words in the file), which is a 
#lot of columns for a CSV to have.

# Perform the necessary imports
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline

# Create a TruncatedSVD instance: svd
svd = TruncatedSVD(n_components=50)

# Create a KMeans instance: kmeans
kmeans = KMeans(n_clusters=6, random_state=42)

# Create a pipeline: pipeline
pipeline = make_pipeline(svd, kmeans)

#End done by DataCamp

# Import pandas
import pandas as pd

# Fit the pipeline to articles
pipeline.fit(articles)

# Calculate the cluster labels: labels
labels = pipeline.predict(articles)

# Create a DataFrame aligning labels and titles: df
df = pd.DataFrame({'label': labels, 'article': titles})

# Display df sorted by cluster label
print(df.sort_values('label'))
