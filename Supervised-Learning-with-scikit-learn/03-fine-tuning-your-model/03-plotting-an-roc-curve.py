'''
Plotting an ROC curve

Great job in the previous exercise - you now have a new addition to your 
toolbox of classifiers!

Classification reports and confusion matrices are great methods to 
quantitatively evaluate model performance, while ROC curves provide a way to 
visually evaluate models. As Hugo demonstrated in the video, most classifiers 
in scikit-learn have a .predict_proba() method which returns the probability 
of a given sample being in a particular class. Having built a logistic 
regression model, you'll now evaluate its performance by plotting an ROC curve. 
In doing so, you'll make use of the .predict_proba() method and become 
familiar with its functionality.

Here, you'll continue working with the PIMA Indians diabetes dataset. The 
classifier has already been fit to the training data and is available as 
logreg.

INSTRUCTIONS
100XP
Import roc_curve from sklearn.metrics.
Using the logreg classifier, which has been fit to the training data, compute 
the predicted probabilities of the labels of the test set X_test. Save the 
result as y_pred_prob.
Use the roc_curve() function with y_test and y_pred_prob and unpack the result 
into the variables fpr, tpr, and thresholds.
Plot the ROC curve with fpr on the x-axis and tpr on the y-axis.
'''
#Done by DataCamp
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('E:\DataCamp\Supervised-Learning-with-scikit-learn\data\diabetes.csv')

X=df.drop(columns=['diabetes'])
y=pd.DataFrame(df['diabetes'])

# Import the necessary modules
from sklearn.linear_model import LogisticRegression

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state=42)

# Create the classifier: logreg
logreg = LogisticRegression()

# Fit the classifier to the training data
logreg.fit(X_train, y_train.values.ravel())
#End done by DataCamp

# Import necessary modules
from sklearn.metrics import roc_curve

# Compute predicted probabilities: y_pred_prob
y_pred_prob = logreg.predict_proba(X_test)[:,1]

# Generate ROC curve values: fpr, tpr, thresholds
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

# Plot ROC curve
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()
