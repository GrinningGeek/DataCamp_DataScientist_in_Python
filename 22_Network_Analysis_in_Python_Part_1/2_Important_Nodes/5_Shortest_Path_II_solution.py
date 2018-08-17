# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:31:48 2018

Shortest Path II
Now that you've got the code for checking whether the destination node is 
present in neighbors, next up, you're going to extend the same function to 
write the code for the condition where the destination node is not present 
in the neighbors.

All the code you need to write is in the else condition; that is, if node2 
is not in neighbors.

INSTRUCTIONS
100 XP
Using the .add() method, add the current node node to the set visited_nodes 
to keep track of what nodes have already been visited.

Add the neighbors of the current node node that have not yet been visited to 
queue. To do this, you'll need to use the .extend() method of queue together 
with a list comprehension. The .extend() method appends all the items in a 
given list.

The output expression and iterator variable of the list comprehension are 
both n. The iterable is the list neighbors, and the conditional is if n is 
not in the visited nodes.
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
            # Add current node to visited nodes
            visited_nodes.add(node)
            
            # Add neighbors of current node that have not yet been visited
            queue.extend([n for n in neighbors if n not in visited_nodes])

