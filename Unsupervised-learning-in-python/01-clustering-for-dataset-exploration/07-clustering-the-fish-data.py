'''
Clustering the fish data

You'll now use your standardization and clustering pipeline from the previous 
exercise to cluster the fish by their measurements, and then create a 
cross-tabulation to compare the cluster labels with the fish species.

As before, samples is the 2D array of fish measurements. Your pipeline is 
available as pipeline, and the species of every fish sample is given by the 
list species.

INSTRUCTIONS
100XP
Import pandas as pd.
Fit the pipeline to the fish measurements samples.
Obtain the cluster labels for samples by using the .predict() method of pipeline.
Using pd.DataFrame(), create a DataFrame df with two columns named 'labels' 
and 'species', using labels and species, respectively, for the column values.
Using pd.crosstab(), create a cross-tabulation ct of df['labels'] and 
df['species'].
'''
#Done by DataCamp
# Perform the necessary imports
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd

# Create scaler: scaler
scaler = StandardScaler()

# Create KMeans instance: kmeans
kmeans = KMeans(n_clusters=4, random_state=42)

# Create pipeline: pipeline
pipeline = make_pipeline(scaler, kmeans)

samples = pd.read_csv('E:/DataCamp/Unsupervised-learning-in-python/data/fish.csv',
                      header=None)

species = samples[0].tolist()

samples = samples.drop(samples.columns[0], axis = 1)

samples = samples.values

#End done by DataCamp

# Fit the pipeline to samples
pipeline.fit(samples)

# Calculate the cluster labels: labels
labels = pipeline.predict(samples)

# Create a DataFrame with labels and species as columns: df
df = pd.DataFrame({'labels': labels, 'species': species})

# Create crosstab: ct
ct = pd.crosstab(df['labels'], df['species'])

# Display ct
print(ct)