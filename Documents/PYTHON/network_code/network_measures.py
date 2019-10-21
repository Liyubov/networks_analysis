#!/usr/bin/env python
# coding: utf-8

# # Big data course 
# @Liubov, Marc
# 
# Second seminar on network theory and applications.
# 
# # Network measures
# 
# Centrality measures for a given network are described in https://en.wikipedia.org/wiki/Centrality 
# 
# Examples of possible local measures: 
# 1. `degree_centrality(G)`, the degree centrality for nodes.
# 2. `in_degree_centrality(G)`, the in-degree centrality for nodes.
# 3. `out_degree_centrality(G)`, the out-degree centrality for nodes
# 4. `betweenness_centrality(G)`, 
# 5. `load_centrality(G)`
# 6. `eigenvector_centrality(G)`
# 
# Other network measures are described in the networkx documentation https://networkx.github.io/documentation/stable/reference/generators.html 

# In[1]:


import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# # Network measures for given networks
# 
# 
# ## Algorithm for measures calculation and visualisation
# 1. Let us first generate a network using networkx standard networks.
# 2. Calculate measures for each node or link of a network
# 3. Plot a network with "nx.draw" https://networkx.github.io/documentation/stable/reference/drawing.html where each node has color according to the node measure
# 4. Plot a network degree sequence as diagram
# 
# **Tips:**
# Be aware of the networkx classes, e.g. `dictionary`, `list` etc.

# In[15]:



# 1. Generate a network
G = nx.star_graph(20)

# 2. Calculate measures for each node
deg = nx.degree_centrality(G) # gives a dictionary!!!
print(type(G.degree))# gives 'networkx.classes.reportviews.DegreeView'
degree_sequence = sorted([d for n, d in G.degree()], reverse=True) # gives array of degree values
 


# 3. Draw network with node colors defined by degree
plt.figure(figsize = (4, 4)) # set size of figure
node_color = degree_sequence # assign node colors
nx.draw(G, node_color = degree_sequence)


# ## Additional information to the plots
# Now we add colorbars for plots.

# In[7]:


# we choose max and min degree for colorbars
vmin = min(degree_sequence) #.min() 
vmax = max(degree_sequence) # .max()
cmap = plt.cm.coolwarm

# we can choose another layouts: layout = nx.fruchterman_reingold_layout(G)


# we plot network with colorbars
nx.draw_networkx(G, node_color=degree_sequence,
                 cmap=cmap, vmin=vmin, vmax=vmax)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm.set_array([])
cbar = plt.colorbar(sm)


# 
# 
# ## Try to plot network measures for your network!
# 
# 1. For a network of your choice try to find network measure which is meaningful.
# 2. Visualise network measures for a network of your choise.

# ## Examples

# In[27]:




G_er = nx.erdos_renyi_graph(20, 0.3)
betw = nx.betweenness_centrality(G_er) #returns dictionary
betw_sequence = np.array(betw.values()) # gives array of degree values
 
print(betw_sequence)
nx.draw(G_er)
#nx.draw_networkx(G_er, node_color = betw_sequence)
plt.show()


# ## Generating your own network 
# 
# You can also create your own network by giving to networkx a matrix or edgelist, or adding nodes and links.
# 
# 
# ## Algorithm
# 1. We first generate a network using matrix, edgelist or load function.
# 2. Then we visualise this network with the simplest function "draw" https://networkx.github.io/documentation/stable/reference/drawing.html
# 
# ## Try to generate your own network!

# In[ ]:




