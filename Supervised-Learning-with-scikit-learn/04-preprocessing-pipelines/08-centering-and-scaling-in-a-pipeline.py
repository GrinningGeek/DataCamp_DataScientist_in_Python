'''
Centering and scaling in a pipeline

With regard to whether or not scaling is effective, the proof is in the 
pudding! See for yourself whether or not scaling the features of 
the White Wine Quality dataset has any impact on its performance. You will use 
a k-NN classifier as part of a pipeline that includes scaling, and for the 
purposes of comparison, a k-NN classifier trained on the unscaled data has 
been provided.

The feature array and target variable array have been pre-loaded as X and y. 
Additionally, KNeighborsClassifier and train_test_split have been imported 
from sklearn.neighbors and sklearn.model_selection, respectively.

INSTRUCTIONS
100XP
Import the following modules:
StandardScaler from sklearn.preprocessing.
Pipeline from sklearn.pipeline.
Complete the steps of the pipeline with StandardScaler() for 'scaler' and 
KNeighborsClassifier() for 'knn'.
Create the pipeline using Pipeline() and steps.
Create training and test sets, with 30% used for testing. Use a random state 
of 42.
Fit the pipeline to the training set.
Compute the accuracy scores of the scaled and unscaled models by using the 
.score() method inside the provided print() functions.
'''
#Done by DataCamp
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('E:/DataCamp/Supervised-Learning-with-scikit-learn/data/white-wine.csv')
X = df.drop('quality', axis=1)
X = X.values

#Make the target variable equal to specifications above
y=pd.DataFrame(df['quality'])
mask = y.quality <= 5
column_name = 'quality'
y.loc[mask, column_name] = True

mask = y.quality > 5
column_name = 'quality'
y.loc[mask, column_name] = False
y = y.values.flatten()

#End done by DataCamp

# Import the necessary modules
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Setup the pipeline steps: steps
steps = [('scaler', StandardScaler()),
        ('knn', KNeighborsClassifier())]
        
# Create the pipeline: pipeline
pipeline = Pipeline(steps)

# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit the pipeline to the training set: knn_scaled
knn_scaled = pipeline.fit(X_train, y_train)

# Instantiate and fit a k-NN classifier to the unscaled data
knn_unscaled = KNeighborsClassifier().fit(X_train, y_train)

# Compute and print metrics
print('Accuracy with Scaling: {}'.format(knn_scaled.score(X_test, y_test)))
print('Accuracy without Scaling: {}'.format(knn_unscaled.score(X_test, y_test)))
