'''
Recommend musical artists part II

Suppose you were a big fan of Bruce Springsteen - which other musicial artists 
might you like? Use your NMF features from the previous exercise and the cosine 
similarity to find similar musical artists. A solution to the previous exercise 
has been run, so norm_features is an array containing the normalized NMF 
features as rows. The names of the musical artists are available as the 
list artist_names.

INSTRUCTIONS
100XP
Import pandas as pd.
Create a DataFrame df from norm_features, using artist_names as an index.
Use the .loc[] accessor of df to select the row of 'Bruce Springsteen'. Assign 
the result to artist.
Apply the .dot() method of df to artist to calculate the dot product of every 
row with artist. Save the result as similarities.
Print the result of the .nlargest() method of similarities to display the 
artists most similar to 'Me First and the Gimme Gimmes'.
'''
#Done by DataCamp
from scipy.sparse import csr_matrix
import numpy as np

music=np.genfromtxt('E:/DataCamp/Unsupervised-learning-in-python/data/Musical_artists/scrobbler-small-sample.csv', 
                    delimiter=',',
                    names=True,
                    dtype=int)

X = music['user_offset']
Y = music['artist_offset']
Z = music['playcount']

def make_music_grid(x, y, z):
    '''
    Takes x, y, z values as lists and returns a 2D numpy array
    Fill with zeros
    Transpose
    '''
    
    grid = np.nan * np.empty((len(set(x)),len(set(y))))
    grid[x, y] = z 
    grid[np.isnan(grid)] = 0
    return grid.T

matrix = make_music_grid(X,Y,Z)            

artists = csr_matrix(matrix)
artists.todense()

# Perform the necessary imports
from sklearn.decomposition import NMF
from sklearn.preprocessing import Normalizer, MaxAbsScaler
from sklearn.pipeline import make_pipeline

# Create a MaxAbsScaler: scaler
scaler = MaxAbsScaler()

# Create an NMF model: nmf
nmf = NMF(n_components=20)

# Create a Normalizer: normalizer
normalizer = Normalizer()

# Create a pipeline: pipeline
pipeline = make_pipeline(scaler, nmf, normalizer)

# Apply fit_transform to artists: norm_features
norm_features = pipeline.fit_transform(artists)


artist_names = pd.read_csv('E:/DataCamp/Unsupervised-learning-in-python/data/Musical_artists/artists.csv', 
                 header=None)

artist_names = artist_names[0].tolist()
#End done by datacamp

# Import pandas
import pandas as pd

# Create a DataFrame: df
df = pd.DataFrame(norm_features, index=artist_names)

# Select row of 'Me first and the gimme gimmes': artist
artist = df.loc['Me First and the Gimme Gimmes']

# Compute cosine similarities: similarities
similarities = df.dot(artist)

# Display those with highest cosine similarity
print(similarities.nlargest())
