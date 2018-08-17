# -*- coding: utf-8 -*-
"""
Subgraphs II
In the previous exercise, we gave you a list of nodes whose neighbors we 
asked you to extract.

Let's try one more exercise in which you extract nodes that have a particular 
metadata property and their neighbors. This should hark back to what you've 
learned about using list comprehensions to find nodes. The exercise will also
build your capacity to compose functions that you've already written before.


INSTRUCTIONS
100 XP

Using a list comprehension, extract nodes that have the metadata 'occupation' 
as 'celebrity' alongside their neighbors:
    
The output expression of the list comprehension is n, and there are two 
iterator variables: n and d. The iterable is the list of nodes of T 
(including the metadata, which you can specify using data=True) and the 
conditional expression is if the 'occupation' key of the metadata dictionary 
d equals 'celebrity'.

Place them in a new subgraph called T_sub. To do this:   
    
Iterate over the nodes, compute the neighbors of each node, and add them to 
the set of nodes nodeset by using the .union() method. This last part has 
been done for you.

Use nodeset along with the T.subgraph() method to calculate T_sub.

Draw T_sub to the screen.

"""
# Import necessary modules
import networkx as nx
import matplotlib as plt

#This step performed for you on DataCamp...
#Data path
path="E:/DataCamp/22_Network_Analysis_in_Python_Part_1/Data/ego-twitter.p"

T = nx.read_gpickle(path)
T=T.to_undirected()
print( "The Twitter network has been loaded as T.")
print("T has been converted to an undirected graph.")

nodes_of_interest = [29, 38, 42]

# Define get_nodes_and_nbrs()
def get_nodes_and_nbrs(G, nodes_of_interest):
    """
    Returns a subgraph of the graph `G` with only the `nodes_of_interest` and their neighbors.
    """
    nodes_to_draw = []
    
    # Iterate over the nodes of interest
    for n in nodes_of_interest:
    
        # Append the nodes of interest to nodes_to_draw
        nodes_to_draw.append(n)
        
        # Iterate over all the neighbors of node n
        for nbr in T.neighbors(n):
        
            # Append the neighbors of n to nodes_to_draw
            nodes_to_draw.append(nbr)
            
    return G.subgraph(nodes_to_draw)

# Extract the subgraph with the nodes of interest: T_draw
T_draw = get_nodes_and_nbrs(T, nodes_of_interest)

# Draw the subgraph to the screen
nx.draw(T_draw)
plt.show()