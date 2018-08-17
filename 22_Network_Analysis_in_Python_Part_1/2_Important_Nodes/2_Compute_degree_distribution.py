# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:31:48 2018

Compute degree distribution
The number of neighbors that a node has is called its "degree", and it's 
possible to compute the degree distribution across the entire graph. In this 
exercise, your job is to compute the degree distribution across T.

INSTRUCTIONS
100 XP
Use a list comprehension along with the .neighbors(n) method to get the 
degree of every node. The result should be a list of integers.

Use n as your iterator variable.

The output expression of your list comprehension should be the number of 
neighbors that node n has - that is, its degree. Use the len() function 
together with the .neighbors() method to compute this.

The iterable in your list comprehension is the all the nodes in T, accessed 
using the .nodes() method.

Print the degrees.
"""
# Import necessary modules
import networkx as nx

#This step performed for you on DataCamp...
#Data path
path="E:/DataCamp/22_Network_Analysis_in_Python_Part_1/Data/ego-twitter.p"

T = nx.read_gpickle(path)
print( "The Twitter network has been loaded as T.")

T = nx.read_gpickle(path)
print( "The Twitter network has been loaded as T.")

# Compute the degree of every node: degrees
degrees = [____]

# Print the degrees

