# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:31:48 2018

NetworkX betweenness centrality on a social network
Betweenness centrality is a node importance metric that uses information about
the shortest paths in a network. It is defined as the fraction of all possible 
shortest paths between any pair of nodes that pass through the node.

NetworkX provides the nx.betweenness_centrality(G) function for computing the 
betweenness centrality of every node in a graph, and it returns a dictionary 
where the keys are the nodes and the values are their betweenness centrality 
measures.

INSTRUCTIONS
100 XP

Compute the betweenness centrality bet_cen of the nodes in the graph T.

Compute the degree centrality deg_cen of the nodes in the graph T.

Compare betweenness centrality to degree centrality by creating a scatterplot 
of the two, with list(bet_cen.values()) on the x-axis and 
list(deg_cen.values()) on the y-axis.
"""
# Import necessary modules
import networkx as nx

#This step performed for you on DataCamp...
#Data path
path="E:/DataCamp/22_Network_Analysis_in_Python_Part_1/Data/ego-twitter.p"

T = nx.read_gpickle(path)
print( "The Twitter network has been loaded as T.")

# Compute the betweenness centrality of T: bet_cen
bet_cen = ____

# Compute the degree centrality of T: deg_cen
deg_cen = ____

# Create a scatter plot of betweenness centrality and degree centrality
____

# Display the plot
plt.show()

