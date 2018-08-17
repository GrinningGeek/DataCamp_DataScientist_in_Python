# -*- coding: utf-8 -*-
"""
Characterizing the network (II)
Let's continue recalling what you've learned before about node importances, 
by plotting the degree distribution of a network. This is the distribution 
of node degrees computed across all nodes in a network.

INSTRUCTIONS
100 XP
Plot the degree distribution of the GitHub collaboration network G. 
Recall that there are four steps involved here:
    
Calculating the degree centrality of G.

Using the .values() method of G and converting it into a list.

Passing the list of degree distributions to plt.hist().

Displaying the histogram with plt.show().

"""
# Import necessary modules
import networkx as nx
import matplotlib.pyplot as plt

#This step performed for you on DataCamp...
#Data path
path="E:/DataCamp/22_Network_Analysis_in_Python_Part_1/Data/github_users.p"

G = nx.read_gpickle(path)
print( "The Twitter network has been loaded as G.")

# Plot the degree distribution of the GitHub collaboration network
plt.hist(list(nx.degree_centrality(G).values()))
plt.show()