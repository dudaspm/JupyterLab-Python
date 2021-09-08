#!/usr/bin/env python
# coding: utf-8

# # Introduction to JupyterLab - 🐘

# ## Where am I? (JupyterLab Notebook)

# Jupyter is a powerful suite of tools that allows us to do many things.
# 
# Jupyter is capable of running **Ju**lia, **Pyt**hon and **R**, as well as some other things. 
# 

# ## Cells

# Each box is called a cell. 

# ### Two types of Cells

# #### Text 

# Text Cells allow you to add text (via Markdown), which includes tables, images, links, bullet lists, numbered lists, LaTeX, blockquote, among other things. 

# ##### Table 
# 
# ```markdown
# | This | is   |
# |------|------|
# |   a  | table| 
# ```
# 
# | This | is   |
# |------|------|
# |   a  | table| 

# ##### Image
# ```markdown
# ![Wheat Field with Cypresses](images/vangogh.jpg)
# ```
# 
# ![Wheat Field with Cypresses](images/vangogh.jpg)
# 
# 
# 
# 

# ##### Link
# ```markdown
# [Attribution](https://www.metmuseum.org/art/collection/search/436535)
# ```
# Vincent van Gogh / Public domain
# The Metropolitan Museum of Art, New York - Purchase, The Annenberg Foundation Gift, 1993 - 
# [Attribution](https://www.metmuseum.org/art/collection/search/436535)

# ##### Bullet List
# ```markdown
# * I am a
#     * bullet
# * list
# ```
# * I am a
#     * bullet
# * list
# 
# 

# ##### Numbered List
# ```markdown
# 1. I am a
#   1. numbered
# 1. list
# ```
# 1. I am a
#   1. numbered
# 1. list

# ##### LaTeX
# ```markdown
# $$e=mc^2$$
# ```
# 
# 
# $$e=mc^2$$

# ##### Blockquotes
# ```markdown
# > This is a blockquote.
# ```
# > This is a blockquote.

# #### Code

# Cells can be run using the Run button &#9658; or selecting one of the run options under the Run menu. 
# 
# Try this out! You can change what is in the cell and rerun the same cell, which is useful for debugging.

# In[1]:


2 + 2 


# **Your turn**: In a new cell, figure out what **5315 + 5618** is. 

# In[2]:


## remove and type out 5315 + 5618
## then hit the play button


# ### Jupyter ✨ MAGIC ✨

# When using other languages in Jupyter/JupyterLab, we need to designate the cell we are using with this langauge or function. To "activate" these language, we need to use ✨ MAGIC ✨. Here are a couple of examples.

# #### HTML

# In[3]:


get_ipython().run_cell_magic('html', '', '<ol>\n  <li>apple</li>\n  <li>banana</li>\n  <li>cookies</li>\n</ol>')


# #### SVG

# In[4]:


get_ipython().run_cell_magic('svg', '', '<svg height="100" width="100">\n  <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="steelblue" />\n</svg>')


# #### R Language

# In Google Colab, you do *not* need to install anything, but if you are going to do this on your local machine (your computer). 
# 
# ![Anaconda Prompt - installing r-essentials](https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/command.PNG)
# 
# You will need to install a few things first. To do this, open up the *Anaconda Prompt (anaconda3)* and run the following two commands:
# 
# ```python
# conda install -c r r-essentials
# ```
# and
# ```python
# conda install -c r rpy2
# ```
# 
# finally, 
# 
# ```python
# %load_ext rpy2.ipython
# ```
# 
# In a new cell, we can then add our R code and see it working. 
# 
# ```R
# %%R
# data <- c(1,2,3)
# print(data)
# ```
# 
# Let's try this out.

# In[5]:


# Let's try here! 


# #### SQL

# In[6]:


get_ipython().run_cell_magic('capture', '', '!pip install ipython-sql')


# What's 
# ```python 
# %%capture
# ```
# ?
# 
# ```python 
# %%capture
# ```
# is another bit of magic that *captures* the output of the cell and does not print it. 

# In[7]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[8]:


get_ipython().run_line_magic('sql', 'sqlite:///exampleDatabase.db')


# In[ ]:




