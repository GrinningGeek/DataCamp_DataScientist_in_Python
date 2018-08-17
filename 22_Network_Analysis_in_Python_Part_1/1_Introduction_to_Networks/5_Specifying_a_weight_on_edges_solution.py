# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:41:09 2018

Specifying a weight on edges
Weights can be added to edges in a graph, typically indicating the "strength" 
of an edge. In NetworkX, the weight is indicated by the 'weight' key in the 
metadata dictionary.

Before attempting the exercise, use the IPython Shell to access the dictionary 
metadata of T and explore it, for instance by running the commands 
T.edge[1][10] and then T.edge[10][1]. Note how there's only one field, and now 
you're going to add another field, called 'weight'.

INSTRUCTIONS
100 XP
Set the 'weight' attribute of the edge between node 1 and 10 of T to be equal 
to 2. Refer to the following template to set an attribute of an edge: 
network_name.edge[node1][node2]['attribute'] = value. Here, the 'attribute'
is 'weight'.

Set the weight of every edge involving node 293 to be equal to 1.1. To do this:
Using a for loop, iterate over all the edges of T, including the metadata.
If 293 is involved in the list of nodes [u, v]:

Set the weight of the edge between u and v to be 1.1.

THIS CODE REQUIRES NETWORKX 1.11 TO WORK
"""

# Import necessary modules
import networkx as nx

#This step performed for you on DataCamp...
#Data path
path="E:/DataCamp/22_Network_Analysis_in_Python_Part_1/Data/ego-twitter.p"

T = nx.read_gpickle(path)
print( "The Twitter network has been loaded as T.")

# Set the weight of the edge
T.edge[1][10]['weight'] = 2

# Iterate over all the edges (with metadata)
for u, v, d in T.edges(data=True):

    # Check if node 293 is involved
    if 293 in [u,v]:
    
        # Set the weight to 1.1
        T.edge[u][v]['weight'] = 1.1