'''
Recommend musical artists part I

In this exercise and the next, you'll use what you've learned about NMF to 
recommend popular music artists! You are given a sparse array artists whose 
rows correspond to artists and whose column correspond to users. The entries 
give the number of times each artist was listened to by each user.

In this exercise, build a pipeline and transform the array into normalized NMF 
features. The first step in the pipeline, MaxAbsScaler, transforms the data so 
that all users have the same influence on the model, regardless of how many 
different artists they've listened to. In the next exercise, you'll use the 
resulting normalized NMF features for recommendation!

This data is part of a larger dataset available here.

INSTRUCTIONS
100XP
Import:
NMF from sklearn.decomposition.
Normalizer and MaxAbsScaler from sklearn.preprocessing.
make_pipeline from sklearn.pipeline.
Create an instance of MaxAbsScaler called scaler.
Create an NMF instance with 20 components called nmf.
Create an instance of Normalizer called normalizer.
Create a pipeline called pipeline that chains together scaler, nmf, and 
normalizer.
Apply the .fit_transform() method of pipeline to artists. Assign the result to 
norm_features.
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
#End done by DataCamp

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