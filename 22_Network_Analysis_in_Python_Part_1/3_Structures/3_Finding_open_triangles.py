# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:31:48 2018

Finding open triangles
Let us now move on to finding open triangles! Recall that they form the basis 
of friend recommendation systems; if "A" knows "B" and "A" knows "C", then 
it's probable that "B" also knows "C".

INSTRUCTIONS
100 XP

Write a function node_in_open_triangle() that has two parameters - G and n - 
and identifies whether a node is present in an open triangle with its 
neighbors.

In the for loop, iterate over all possible triangle relationship combinations.

If the nodes n1 and n2 do not have an edge between them, set in_open_triangle 
to True, break out from the if statement and return in_open_triangle.

Use this function to count the number of open triangles that exist in T.

In the for loop, iterate over all the nodes in T.

If the current node n is in an open triangle, increment num_open_triangles.

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

from itertools import combinations

# Define node_in_open_triangle()
def node_in_open_triangle(G, n):
    """
    Checks whether pairs of neighbors of node `n` in graph `G` are in an 'open triangle' relationship with node `n`.
    """
    in_open_triangle = False
    
    # Iterate over all possible triangle relationship combinations
    for n1, n2 in ____:
    
        # Check if n1 and n2 do NOT have an edge between them
        if not ____:
        
            in_open_triangle = ____
            
            break
            
    return ____

# Compute the number of open triangles in T
num_open_triangles = 0

# Iterate over all the nodes in T
for n in ____:

    # Check if the current node is in an open triangle
    if ____:
    
        # Increment num_open_triangles
        ____ += 1
        
print(num_open_triangles)