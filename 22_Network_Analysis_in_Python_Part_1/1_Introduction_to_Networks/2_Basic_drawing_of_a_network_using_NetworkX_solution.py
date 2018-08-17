# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:41:09 2018

Exercise
Basic drawing of a network using NetworkX
NetworkX provides some basic drawing functionality that works for small graphs.
We have selected a subset of nodes from the graph for you to practice using 
NetworkX's drawing facilities. It has been pre-loaded as T_sub.

Instructions 100XP
Import matplotlib.pyplot as plt and networkx as nx.

Draw T_sub to the screen by using the nx.draw() function, and don't forget to 
also use plt.show() to display it.

THIS CODE REQUIRES NETWORKX 1.11 TO WORK
"""

# Import necessary modules
import matplotlib.pyplot as plt
import networkx as nx

#This step performed for you on DataCamp...
#Data path
path="E:/DataCamp/22_Network_Analysis_in_Python_Part_1/Data/ego-twitter.p"

T = nx.read_gpickle(path)
print( "The Twitter network has been loaded as T.")
T_sub = T.subgraph(list(range(0,50)))

# Draw the graph to screen
nx.draw(T_sub)
plt.show()