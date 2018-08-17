# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:31:48 2018

Deep dive - Twitter network part II
Next, you're going to do an analogous deep dive on betweenness centrality! 
Just a few hints to help you along: remember that betweenness centrality is 
computed using nx.betweenness_centrality(G).

INSTRUCTIONS
100 XP
Write a function find_node_with_highest_bet_cent(G) that returns the node(s) 
with the highest betweenness centrality.

Compute the betweenness centrality of G.

Compute the maximum betweenness centrality using the max() function on list
(bet_cent.values()).

Iterate over the degree centrality dictionary, bet_cent.items().

If the degree centrality value v of the current node k is equal to max_bc, add 
it to the set of nodes.

Use your function to find the node(s) that has the highest betweenness 
centrality in T.

Write an assertion statement that you've got the right node. This has been 
done for you, so hit 'Submit Answer' to see the result!
"""
# Import necessary modules
import networkx as nx

#This step performed for you on DataCamp...
#Data path
path="E:/DataCamp/22_Network_Analysis_in_Python_Part_1/Data/ego-twitter.p"

T = nx.read_gpickle(path)
print( "The Twitter network has been loaded as T.")

# Define find_node_with_highest_bet_cent()
def find_node_with_highest_bet_cent(G):

    # Compute betweenness centrality: bet_cent
    bet_cent = ____
    
    # Compute maximum betweenness centrality: max_bc
    max_bc = ____
    
    nodes = set()
    
    # Iterate over the betweenness centrality dictionary
    for k, v in ____:
    
        # Check if the current value has the maximum betweenness centrality
        if ____ == ____:
        
            # Add the current node to the set of nodes
            ____
            
    return nodes

# Use that function to find the node(s) that has the highest betweenness centrality in the network: top_bc
top_bc = ____

# Write an assertion statement that checks that the node(s) is/are correctly identified.
for node in top_bc:
    assert nx.betweenness_centrality(T)[node] == max(nx.betweenness_centrality(T).values())
