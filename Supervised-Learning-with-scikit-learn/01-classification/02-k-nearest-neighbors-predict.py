'''
k-Nearest Neighbors: Predict

Having fit a k-NN classifier, you can now use it to predict the label of a new 
data point. However, there is no unlabeled data available since all of it was 
used to fit the model! You can still use the .predict() method on the X that 
was used to fit the model, but it is not a good indicator of the model's 
ability to generalize to new, unseen data.

In the next video, Hugo will discuss a solution to this problem. For now, a 
random unlabeled data point has been generated and is available to you as 
X_new. You will use your classifier to predict the label for this new data 
point, as well as on the training data X that the model has already seen. 
Using .predict() on X_new will generate 1 prediction, while using it on X 
will generate 435 predictions: 1 for each sample.

The DataFrame has been pre-loaded as df. This time, you will create the 
feature array X and target variable array y yourself.

INSTRUCTIONS
100XP
Create arrays for the features and the target variable from df. As a 
reminder, the target variable is 'party'.

Instantiate a KNeighborsClassifier with 6 neighbors.
Fit the classifier to the data.
Predict the labels of the training data, X.
Predict the label of the new data point X_new.
'''
#Performed by DataCamp
import pandas as pd

df = pd.read_csv('E:/DataCamp/Supervised-Learning-with-scikit-learn/data/house-votes-84.csv', 
                 header=None)
df.columns = ['party', 'infants', 'water', 'budget', 'physician', 'salvador',
              'religious', 'satellite', 'aid', 'missile', 'immigration', 
              'synfuels', 'education', 'superfund', 'crime', 
              'duty_free_exports', 'eaa_rsa']

df = df.replace({'y': 1, 'n':0, '?':0})

X_new = [0.845363,0.924887,0.702607,0.922102,0.56495,0.167178,0.683887,
         0.054724,0.644309,0.53251,0.223809,0.487974,0.319001,0.689787,
         0.630383,0.560107]
X_new = pd.DataFrame([X_new])

#End Performed by DataCamp

# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier 

# Create arrays for the features and the response variable
y = df['party'].values
X = df.drop('party', axis=1).values

# Create a k-NN classifier with 6 neighbors: knn
knn = knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
knn.fit(X,y)

# Predict the labels for the training data X
y_pred = knn.predict(X)

# Predict and print the label for the new data point X_new
new_prediction = knn.predict(X_new)
print("Prediction: {}".format(new_prediction))
