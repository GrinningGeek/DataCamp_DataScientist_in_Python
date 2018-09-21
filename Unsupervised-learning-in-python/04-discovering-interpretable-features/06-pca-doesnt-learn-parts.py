'''
PCA doesn't learn parts

Unlike NMF, PCA doesn't learn the parts of things. Its components do not 
correspond to topics (in the case of documents) or to parts of images, when 
trained on images. Verify this for yourself by inspecting the components of a 
PCA model fit to the dataset of LED digit images from the previous exercise. 
The images are available as a 2D array samples. Also available is a modified 
version of the show_as_image() function which colors a pixel red if the value 
is negative.

After submitting the answer, notice that the components of PCA do not 
represent meaningful parts of images of LED digits!

INSTRUCTIONS
100XP
Import PCA from sklearn.decomposition.
Create a PCA instance called model with 7 components.
Apply the .fit_transform() method of model to samples. Assign the result to 
features.
To each component of the model (accessed via model.components_), apply the 
show_as_image() function to that component inside the loop.
'''
#Done by DataCamp
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

samples = pd.read_csv('E:/DataCamp/Unsupervised-learning-in-python/data/lcd-digits.csv',
                      header=None)

def show_as_image(vector):
#Given a 1d vector representing an image, display that image in
#black and white.  If there are negative values, then use red for 
#that pixel.
    bitmap = vector.reshape((13, 8))  
    
    # make a square array
    bitmap /= np.abs(vector).max()  
    
    # normalise
    bitmap = bitmap[:,:,np.newaxis]
    
    rgb_layers = [np.abs(bitmap)] + [bitmap.clip(0)] * 2
    rgb_bitmap = np.concatenate(rgb_layers, axis=-1)
    plt.imshow(rgb_bitmap, interpolation='nearest')
    plt.xticks([])
    plt.yticks([])
    plt.show()

#End done by DataCamp

# Import PCA
from sklearn.decomposition import PCA

# Create a PCA instance: model
model = PCA(n_components=7)

# Apply fit_transform to samples: features
features = model.fit_transform(samples)

# Call show_as_image on each component
for component in model.components_:
    show_as_image(component)
    