# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:41:09 2018

Visualizing using Circos plots
Circos plots are a rational, non-cluttered way of visualizing graph data, in 
which nodes are ordered around the circumference in some fashion, and the 
edges are drawn within the circle that results, giving a beautiful as well as 
informative visualization about the structure of the network.

In this exercise, you'll continue getting practice with the nxviz API, this 
time with the CircosPlot object. matplotlib.pyplot has been imported for you 
as plt.

INSTRUCTIONS
100 XP

Import CircosPlot from nxviz.

Plot the Twitter network T as a Circos plot without any styling. Use the 
CircosPlot() function to do this. Don't forget to draw it to the screen using
.draw() and then display it using plt.show().

THIS CODE REQUIRES NETWORKX 1.11 TO WORK
"""

# Import necessary modules
import networkx as nx

#This step performed for you on DataCamp...
T = nx.read_gpickle("ego-twitter.p")
print("The Twitter network has been loaded as 'T'")

# Import necessary modules
import matplotlib.pyplot as plt
____

# Create the CircosPlot object: c
c = ____

# Draw c to the screen
____

# Display the plot
____