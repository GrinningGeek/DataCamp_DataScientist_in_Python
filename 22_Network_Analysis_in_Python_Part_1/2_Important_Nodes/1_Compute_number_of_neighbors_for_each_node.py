# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:31:48 2018

Compute number of neighbors for each node
How do you evaluate whether a node is an important one or not? There are a 
ways to do so, and here, you're going to look at one metric: the number of 
neighbors that a node has.

Every NetworkX graph G exposes a .neighbors(n) method that returns a list of 
nodes that are the neighbors of the node n. To begin, use this method in the 
IPython Shell on the Twitter network T to get the neighbors of of node 1. This 
will get you familiar with how the function works. Then, your job in this 
exercise is to write a function that returns all nodes that have m neighbors.

INSTRUCTIONS
100 XP
Write a function called nodes_with_m_nbrs() that has two parameters - G and 
m - and returns all nodes that have m neighbors. To do this:
    
Iterate over all nodes in G (not including the metadata).

Use the len() function together with the .neighbors() method to calculate the 
total number of neighbors that node n in graph G has.

If the number of neighbors of node n is equal to m, add n to the set nodes 
using the .add() method.

After iterating over all the nodes in G, return the set nodes.
Use your nodes_with_m_nbrs() function to retrieve all the nodes that have 
6 neighbors in the graph T.
"""

import networkx as nx
print ("NetworkX has been loaded as nx.")

#This step performed for you on DataCamp...
#Data path
path="E:/DataCamp/22_Network_Analysis_in_Python_Part_1/Data/ego-twitter.p"

T = nx.read_gpickle(path)
print( "The Twitter network has been loaded as T.")

# Define nodes_with_m_nbrs()
def ____:
    """
    Returns all nodes in graph G that have m neighbors.
    """
    nodes = set()
    
    # Iterate over all nodes in G
    for n in ____:
    
        # Check if the number of neighbors of n matches m
        if ____ == ____:
        
            # Add the node n to the set
            ____
            
    # Return the nodes with m neighbors
    return nodes

# Compute and print all nodes in T that have 6 neighbors
six_nbrs = ____
print(____)