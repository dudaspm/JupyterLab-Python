#!/usr/bin/env python
# coding: utf-8

# In[1]:


import graphviz
dot = graphviz.Digraph()

# Add nodes
dot.node('A', 'Content')
dot.node('B', 'drive')
dot.node('C', 'MyDrive')

# Add edges
dot.edges(['AB','BC'])

# Visualize the graph
dot


# In[ ]:




