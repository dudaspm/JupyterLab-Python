#!/usr/bin/env python
# coding: utf-8

# # All About Google Colab and JupyterLab

# ## Working with Data 
# {cite:ps}`GoogleColaboratoryIO`
# 

# ### A Temporary Solution
# 
# You can create and interactive with files when you access Google Colab, *BUT* they will disappear after your session ends. An example would be:

# In[1]:


f = open("thanosSnapping.txt", "a")
f.write("you should've gone for the head")
f.close()


# ```{warning} 
# Super serious here. 
# If files are not written to your local machine or your Google Drive. They will be **gone** the next time you log-in.
# ```

# We need a better solution for this. So, let's take a look at these options. 

# ### Connecting to Your Google Drive
# 
# There are two ways to connect to your Google Drive. 
# 
# #### Selecting the Icon to Connect
# 
# ```{image} https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/connectToDrive.PNG
# :alt: Icon for Connecting to Google Colab
# :width: 400px
# :align: center
# ```
# 
# #### Connecting Using Google Colab Code
# 
# ```python
# from google.colab import drive
# drive.mount('/content/drive')
# ```
# 
# This will look something like this:
# 
# ```{image} https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/googleColabConnect.PNG
# :alt: Connecting to Google Colab with Code
# :width: 500px
# :align: center
# ```

# #### I am Connected, Now What?
# 
# It can be a bit difficult to figure out where to place files and where your files are located at in Google Colab. Once you connect you will need to navigate 

# In[2]:


get_ipython().run_cell_magic('capture', '', '!pip install graphviz')


# In[3]:


import graphviz
dot = graphviz.Digraph(graph_attr={'rankdir':'LR'}, engine="neato")

# Add nodes
dot.node('A', 'Content', shape="folder", pos='0,3!')
dot.node('B', 'drive', shape="folder", pos='1,2!')
dot.node('C', 'MyDrive', shape="folder", pos='2,1!')

# Add edges
dot.edges(['AB','BC'])

# Visualize the graph
dot 


# In[ ]:




