# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:41:09 2018

Checking the un/directed status of a graph
In the video, Eric described to you different types of graphs. Which type of 
graph do you think the Twitter network data you have been working with 
corresponds to? Use Python's built-in type() function in the IPython Shell to 
find out. The network, as before, has been pre-loaded as T.

Of the four below choices below, which one corresponds to the type of graph 
that T is?

INSTRUCTIONS
50 XP
Possible Answers
Undirected Graph.
Directed Graph.             
Undirected Multi-Edge Graph.
Directed Multi-Edge Graph.

THIS CODE REQUIRES NETWORKX 1.11 TO WORK
"""

# Import necessary modules
import networkx as nx

#This step performed for you on DataCamp...
#Data path
path="E:/DataCamp/22_Network_Analysis_in_Python_Part_1/Data/ego-twitter.p"

T = nx.read_gpickle(path)
print( "The Twitter network has been loaded as T.")