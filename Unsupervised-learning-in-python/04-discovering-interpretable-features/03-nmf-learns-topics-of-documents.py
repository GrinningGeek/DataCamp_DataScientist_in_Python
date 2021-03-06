'''
NMF learns topics of documents

In the video, you learned when NMF is applied to documents, the components 
correspond to topics of documents, and the NMF features reconstruct the 
documents from the topics. Verify this for yourself for the NMF model that you 
built earlier using the Wikipedia articles. Previously, you saw that the 3rd 
NMF feature value was high for the articles about actors Anne Hathaway and 
Denzel Washington. In this exercise, identify the topic of the corresponding 
NMF component.

The NMF model you built earlier is available as model, while words is a list 
of the words that label the columns of the word-frequency array.

After you are done, take a moment to recognise the topic that the articles 
about Anne Hathaway and Denzel Washington have in common!

INSTRUCTIONS
100XP
Import pandas as pd.
Create a DataFrame components_df from model.components_, setting columns=words 
so that columns are labeled by the words.
Print components_df.shape to check the dimensions of the DataFrame.
Use the .iloc[] accessor on the DataFrame components_df to select row 3. 
Assign the result to component.
Call the .nlargest() method of component, and print the result. This gives the 
five words with the highest values for that component.
'''
#Done by DataCamp
import pandas as pd
from scipy.sparse import csr_matrix

df = pd.read_csv('E:/DataCamp/Unsupervised-learning-in-python/data/Wikipedia_articles/wikipedia-vectors.csv', 
                 index_col=0)

words = pd.read_csv('E:/DataCamp/Unsupervised-learning-in-python/data/Wikipedia_articles/wikipedia-vocabulary-utf8.txt', 
                 delimiter='\n', header=None)

articles = csr_matrix(df.transpose())
titles = list(df.columns)

# Import NMF
from sklearn.decomposition import NMF

# Create an NMF instance: model
model = NMF(n_components=6, random_state=42)

# Fit the model to articles
model.fit(articles)

# Transform the articles: nmf_features
nmf_features = model.transform(articles)

#End done by DataCamp



# Import pandas
import pandas as pd

# Create a DataFrame: components_df
components_df = pd.DataFrame(model.components_, columns=words)

# Print the shape of the DataFrame
print(components_df.shape)

# Select row 3: component
component = components_df.iloc[3]

# Print result of nlargest
print(component.nlargest())
