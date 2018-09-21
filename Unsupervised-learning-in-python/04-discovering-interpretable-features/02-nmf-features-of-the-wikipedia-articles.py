'''
NMF features of the Wikipedia articles

Now you will explore the NMF features you created in the previous exercise. 
A solution to the previous exercise has been pre-loaded, so the array 
nmf_features is available. Also available is a list titles giving the title of 
each Wikipedia article.

When investigating the features, notice that for both actors, the NMF feature 
3 has by far the highest value. This means that both articles are reconstructed 
using mainly the 3rd NMF component. In the next video, you'll see why: NMF 
components represent topics (for instance, acting!).

INSTRUCTIONS
100XP
Import pandas as pd.
Create a DataFrame df from nmf_features using pd.DataFrame(). Set the index to 
titles using index=titles.
Use the .loc[] accessor of df to select the row with title 'Anne Hathaway', 
and print the result. These are the NMF features for the article about the 
actress Anne Hathaway.
Repeat the last step for 'Denzel Washington' (another actor).
'''
#Done by DataCamp
import pandas as pd
from scipy.sparse import csr_matrix

df = pd.read_csv('E:/DataCamp/Unsupervised-learning-in-python/data/Wikipedia_articles/wikipedia-vectors.csv', 
                 index_col=0)
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

# Create a pandas DataFrame: df
df = pd.DataFrame(nmf_features, index=titles)

# Print the row for 'Anne Hathaway'
print(df.loc['Anne Hathaway'])

# Print the row for 'Denzel Washington'
print(df.loc['Denzel Washington'])
