#!/usr/bin/env python
# coding: utf-8

# # Big data course 
# @Liubov, Marc
# 
# Second seminar on network theory and applications.
# Most of the materials are described in the networkx documentation https://networkx.github.io/documentation/stable/reference/generators.html 

# In[1]:


import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# # Network classes
# We start we several classes of random networks. The simplest one is complete graph. 
# 
# ## Algorithm
# 1. We first generate a network using preassigned class.
# 2. Then we visualise this network with the simplest function "draw" https://networkx.github.io/documentation/stable/reference/drawing.html 

# In[4]:



G = nx.complete_graph(20)
# draw uses the preassigned layout
nx.draw(G)


# ## Network classes 
# Other pre-assigned network classes return:
# 
# 1. balanced_tree(r, h[, create_using]), the perfectly balanced r-ary tree of height h.
# 2. barbell_graph(m1, m2[, create_using]), the Barbell Graph: two complete graphs connected by a path.
# 3. binomial_tree(n), the Binomial Tree of order n.
# 4. complete_graph(n[, create_using]), the complete graph K_n with n nodes.
# 5. complete_multipartite_graph(*subset_sizes), the complete multipartite graph with the specified subset sizes.
# 6. circular_ladder_graph(n[, create_using]), the circular ladder graph \(CL_n\) of length n.
# 7. circulant_graph(n, offsets[, create_using]), the circulant graph \(Ci_n(x_1, x_2, ..., x_m)\) with \(n\) vertices.
# 8. cycle_graph(n[, create_using]), the cycle graph \(C_n\) of cyclically connected nodes.
# 9. dorogovtsev_goltsev_mendes_graph(n[, …]), the hierarchically constructed Dorogovtsev-Goltsev-Mendes graph.
# 10. empty_graph([n, create_using, default]), the empty graph with n nodes and zero edges.
# 11. full_rary_tree(r, n[, create_using]), a full r-ary tree of n vertices.
# 12. ladder_graph(n[, create_using]), the Ladder graph of length n.
# 13. lollipop_graph(m, n[, create_using]), the Lollipop Graph; K_m connected to P_n.
# 14. path_graph(n[, create_using]),  the Path graph P_n of linearly connected nodes.
# 15. star_graph(n[, create_using]), the star graph
# 16. trivial_graph([create_using]), the Trivial graph with one node (with label 0) and no edges.
# 17. turan_graph(n, r), the Turan Graph
# 18. wheel_graph(n[, create_using]), the wheel graph
# 
# 
# ## Try to choose your own network!
# 
# These networks are deterministic (are generated with deterministic prescribed rules).

# ## Random networks generation

# In[6]:




G_rg = nx.random_geometric_graph(500, 0.1)

G_er = nx.erdos_renyi_graph(20, 0.3)

nx.draw(G_rg)
plt.show()

nx.draw(G_er)
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




