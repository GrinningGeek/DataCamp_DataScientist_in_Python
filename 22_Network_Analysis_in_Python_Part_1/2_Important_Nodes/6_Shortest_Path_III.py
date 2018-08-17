# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:31:48 2018

Shortest Path III
This is the final exercise of this trio! You're now going to complete the 
problem by writing the code that returns False if there's no path between 
two nodes.

INSTRUCTIONS
100 XP

Check to see if the queue has been emptied. You can do this by inspecting the 
last element of queue with [-1].

Place the appropriate return statement for indicating whether there's a path 
between these two nodes.
"""
# Import necessary modules
import networkx as nx

#This step performed for you on DataCamp...
#Data path
path="E:/DataCamp/22_Network_Analysis_in_Python_Part_1/Data/ego-twitter.p"

T = nx.read_gpickle(path)
print( "The Twitter network has been loaded as T.")

def path_exists(G, node1, node2):
    """
    This function checks whether a path exists between two nodes (node1, node2) in graph G.
    """
    visited_nodes = set()
    queue = [node1]
    
    for node in queue:  
        neighbors = G.neighbors(node)
        if node2 in neighbors:
            print('Path exists between nodes {0} and {1}'.format(node1, node2))
            return True
            break

        else:
            visited_nodes.add(node)
            queue.extend([n for n in neighbors if n not in visited_nodes])
        
        # Check to see if the final element of the queue has been reached
        if node == ____:
            print('Path does not exist between nodes {0} and {1}'.format(node1, node2))

            # Place the appropriate return statement
            return ____

