# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:31:48 2018

Finding all maximal cliques of size "n"
Now that you've explored triangles (and open triangles), let's move on to the 
concept of maximal cliques. Maximal cliques are cliques that cannot be 
extended by adding an adjacent edge, and are a useful property of the graph 
when finding communities. NetworkX provides a function that allows you to 
identify the nodes involved in each maximal clique in a graph: 
nx.find_cliques(G). Play around with the function by using it on T in the 
IPython Shell, and then try answering the exercise.

INSTRUCTIONS
100 XP

Write a function maximal_cliques() that has two parameters - G and size - 
and finds all maximal cliques of size n.

In the for loop, iterate over all the cliques in G using the nx.find_cliques() 
function.

If the current clique is of size size, append it to the list mcs.

Use an assert statement and your maximal_cliques() function to check that 
there are 33 maximal cliques of size 3 in the graph T.

"""
# Import necessary modules
import networkx as nx

#This step performed for you on DataCamp...
#Data path
path="E:/DataCamp/22_Network_Analysis_in_Python_Part_1/Data/ego-twitter.p"

T = nx.read_gpickle(path)
T = T.subgraph(list(range(0,50)))
T=T.to_undirected()
print( "A subsampled version of the Twitter network has been loaded as T.")
print("T has been converted to an undirected graph.")

# Define maximal_cliques()
def maximal_cliques(G,size):
    """
    Finds all maximal cliques in graph `G` that are of size `size`.
    """
    mcs = []
    for clique in nx.find_cliques(G):
        if len(clique) == size:
            mcs.append(clique)
    return mcs

# Check that there are 33 maximal cliques of size 3 in the graph T
assert len(maximal_cliques(T,3)) == 33