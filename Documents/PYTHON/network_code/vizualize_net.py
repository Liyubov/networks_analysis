import numpy as np # linear algebra
#import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#import pydicom
#import os
#import scipy.ndimage
import matplotlib.pyplot as plt
import networkx as nx

#########################
print('Assign parameter values')
#########################
n = 500; # number of nodes
p=0.5; #parameter value for SF net 
src_vertex = 1; #source node in the network
k = 8 # patameter of WS network
beta = 0.2 #rewiring parameter for WS net


#########################  import matrices 
#A=np.matrix([[1,1],[2,1]])
#A_lond = np.load('Londonmatr.txt)

######################### initialize graph
#G=nx.Graph()
#G=nx.erdos_renyi_graph(n, p, seed=None, directed=False)
#G=nx.scale_free_graph(n, alpha=0.5, beta=0.4, gamma=0.1);#, delta_in=0.2, delta_out=0, create_using=None, seed=None)
G=nx.watts_strogatz_graph(n, k, beta, seed=None)
#G=nx.from_numpy_matrix(A)


nx.draw(G) #draw the network itself

nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
edges = G.edges()
nx.draw_networkx_edges(G,pos,
                       edgelist=edges,
                       width=1,alpha=0.5,edge_color='indigo')
plt.show() 				   

