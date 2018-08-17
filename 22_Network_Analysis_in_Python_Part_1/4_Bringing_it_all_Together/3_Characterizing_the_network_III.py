# -*- coding: utf-8 -*-
"""
Characterizing the network (III)
The last exercise was on degree centrality; this time round, let's recall 
betweenness centrality!

A small note: if executed correctly, this exercise may need about 5 
seconds to execute.

INSTRUCTIONS
100 XP

Plot the betweenness centrality distribution of the GitHub collaboration 
network. You have to follow exactly the same four steps as in the previous 
exercise, substituting nx.betweenness_centrality() in place of 
nx.degree_centrality().

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
____
____