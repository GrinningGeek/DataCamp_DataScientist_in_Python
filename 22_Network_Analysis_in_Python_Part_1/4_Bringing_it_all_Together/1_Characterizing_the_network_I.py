# -*- coding: utf-8 -*-
"""
Characterizing the network (I)
To start out, let's do some basic characterization of the network, by looking 
at the number of nodes and number of edges in a network. It has been 
pre-loaded as G and is available for exploration in the IPython Shell. Your 
job in this exercise is to identify how many nodes and edges are present in 
the network. You can use the functions len(G.nodes()) and len(G.edges()) to 
calculate the number of nodes and edges respectively.

INSTRUCTIONS
50 XP

Possible Answers
74095 nodes, 56519 edges.
56519 nodes, 74095 edges.   
47095 nodes, 65789 edges.
63762 nodes, 71318 edges.

"""
# Import necessary modules
import networkx as nx

#This step performed for you on DataCamp...
#Data path
path="E:/DataCamp/22_Network_Analysis_in_Python_Part_1/Data/github_users.p"

G = nx.read_gpickle(path)
print( "The Twitter network has been loaded as G.")