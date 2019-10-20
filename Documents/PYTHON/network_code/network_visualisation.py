#!/usr/bin/env python
# coding: utf-8

# # Big data course 
# @Liubov, Marc
# 
# Second seminar on network theory and applications

# In[1]:


import json
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


g = nx.karate_club_graph()
fig, ax = plt.subplots(1, 1, figsize=(8, 6));
nx.draw_networkx(g, ax=ax)


# ## Additional visualisation 
#  Now, we're going to display this graph in the notebook with D3.js. The first step is to bring this graph to JavaScript. Here, we choose to export the graph to JSON. 
# 

# In[5]:



nodes = [{'name': str(i), 'club': g.node[i]['club']}
         for i in g.nodes()]
links = [{'source': u[0], 'target': u[1]}
         for u in g.edges()]
with open('graph.json', 'w') as f:
    json.dump({'nodes': nodes, 'links': links},
              f, indent=4,)


# Next we create html
# <div id="d3-example"></div>
# <style>
# .node {stroke: #fff; stroke-width: 1.5px;}
# .link {stroke: #999; stroke-opacity: .6;}
# </style>

# In[ ]:




