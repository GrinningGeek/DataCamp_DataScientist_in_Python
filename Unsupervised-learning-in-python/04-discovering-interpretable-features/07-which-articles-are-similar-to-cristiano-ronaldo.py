'''
Which articles are similar to 'Cristiano Ronaldo'?

In the video, you learned how to use NMF features and the cosine similarity to 
find similar articles. Apply this to your NMF model for popular Wikipedia 
articles, by finding the articles most similar to the article about the 
footballer Cristiano Ronaldo. The NMF features you obtained earlier are 
available as nmf_features, while titles is a list of the article titles.

INSTRUCTIONS
100XP
Import normalize from sklearn.preprocessing.
Apply the normalize() function to nmf_features. Store the result as 
norm_features.
Create a DataFrame df from norm_features, using titles as an index.
Use the .loc[] accessor of df to select the row of 'Cristiano Ronaldo'. Assign 
the result to article.
Apply the .dot() method of df to article to calculate the cosine similarity of 
every row with article.
Print the result of the .nlargest() method of similarities to display the most 
similiar articles. This has been done for you, so hit 'Submit Answer' to see 
the result!
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

# Perform the necessary imports
import pandas as pd
from sklearn.preprocessing import normalize

# Normalize the NMF features: norm_features
norm_features = normalize(nmf_features)

# Create a DataFrame: df
df = pd.DataFrame(norm_features, index=titles)

# Select the row corresponding to 'Cristiano Ronaldo': article
article = df.loc['Cristiano Ronaldo']

# Compute the dot products: similarities
similarities = df.dot(article)

# Display those with the largest cosine similarity
print(similarities.nlargest())