# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:31:48 2018

Shortest Path I
You can leverage what you know about finding neighbors to try finding paths in 
a network. One algorithm for path-finding between two nodes is the 
"breadth-first search" (BFS) algorithm. In a BFS algorithm, you start from a 
particular node and iteratively search through its neighbors and neighbors' 
neighbors until you find the destination node.

Pathfinding algorithms are important because they provide another way of 
assessing node importance; you'll see this in a later exercise.

In this set of 3 exercises, you're going to build up slowly to get to the 
final BFS algorithm. The problem has been broken into 3 parts that, if you 
complete in succession, will get you to a first pass implementation of the 
BFS algorithm.

INSTRUCTIONS
100 XP

Create a function called path_exists() that has 3 parameters - G, node1, and 
node2 - and returns whether or not a path exists between the two nodes.

Initialize the queue of cells to visit with the first node, node1. queue 
should be a list`.

Iterate over the nodes in queue.

Get the neighbors of the node using the .neighbors() method of the graph G.
Check to see if the destination node node2 is in the set of neighbors. If it 
is, return True.
"""
# Import necessary modules
import networkx as nx

#This step performed for you on DataCamp...
#Data path
path="E:/DataCamp/22_Network_Analysis_in_Python_Part_1/Data/ego-twitter.p"

T = nx.read_gpickle(path)
print( "The Twitter network has been loaded as T.")

# Define path_exists()
def ____:
    """
    This function checks whether a path exists between two nodes (node1, node2) in graph G.
    """
    visited_nodes = set()
    
    # Initialize the queue of cells to visit with the first node: queue
    queue = ____  
    
    # Iterate over the nodes in the queue
    for node in ____:
    
        # Get neighbors of the node
        neighbors = ____ 

