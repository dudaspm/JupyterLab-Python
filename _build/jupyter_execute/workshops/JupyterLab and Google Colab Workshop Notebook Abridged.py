#!/usr/bin/env python
# coding: utf-8

# # JupyterLab and Google Colab Workshop Notebook Abridged

# ## Notebook Introduction - 🐸

# ### How to Use this Notebook 

# This notebook allows you to both follow the text and interact with the code directly. 
# 
# At the top page, you will see:
# 
# <img src="https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/topscreen1.png" alt="icons at the top right corner of the screen" style="width:200px;margin-left:auto;margin-right:auto;display:block;">
# 
# Select the icon on the left, the rocket ship:
# 
# <img src="https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/topscreen2.png" alt="rocket ship icon for running the notebook" style="width:200px;margin-left:auto;margin-right:auto;display:block;">
# 
# Then go down to "Live Code":
# 
# 
# <img src="https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/topscreen4.png" alt="selecting Live Code" style="width:240px;margin-left:auto;margin-right:auto;display:block;">
# 
# You should see at the top of the page a loading bar that cycles through mulitple states. 
# <img src="https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/topscreen6.png" alt="loading bar, first cycle" style="width:240px;margin-left:auto;margin-right:auto;display:block;">
# 
# <img src="https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/topscreen7.png" alt="loading bar, second cycle" style="width:240px;margin-left:auto;margin-right:auto;display:block;">
# 
# <img src="https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/topscreen7b.png" alt="loading bar, thrid cycle" style="width:240px;margin-left:auto;margin-right:auto;display:block;">
# 
# <img alt="loading bar, fourth cycle" src="https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/topscreen8.png" style="width:240px;margin-left:auto;margin-right:auto;display:block;">
# 
# Then, finally:
# <img src="https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/topscreen9.png" alt="loading bar, final cycle" style="width:240px;margin-left:auto;margin-right:auto;display:block;">
# 
# Try this for yourself! 
# 
# Here is a basic line in Python, after setting to Live Code. You can edit the Python code **directly in the notebook** 😀 😀 😀

# In[1]:


2 + 2


# ## Export to Binder or Google Colab 

# As you can see you can also export these notebooks to Binder or Google Colab. 
# 
# <img alt="Binder or Google Colab options" src="https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/topscreen3.png" style="width:240px;margin-left:auto;margin-right:auto;display:block;">
# 
# This will take you to their respective websites but you can work with them there, if you would like!

# ### References

# I know it tradition to have the refences at the end of books, but when you are standing on the shoulders of giants. You thank them first. 

# ```{bibliography}
# ```

# ### Thank you!
# 
# Also, a huge *thank you* to Adam Lavely (https://github.com/adamlavely) for developing some of the intial notebooks! 

# ## Introduction to JupyterLab - 🐘

# ### Where am I? (JupyterLab Notebook)

# Jupyter is a powerful suite of tools that allows us to do many things.
# 
# Jupyter is capable of running **Ju**lia, **Pyt**hon and **R**, as well as some other things. 
# 

# ### Cells

# Each box is called a cell. 

# #### Two types of Cells

# ##### Text 

# Text Cells allow you to add text (via Markdown), which includes tables, images, links, bullet lists, numbered lists, LaTeX, blockquote, among other things. 

# ###### Table 
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

# ###### Image
# ```markdown
# ![Wheat Field with Cypresses](images/vangogh.jpg)
# ```
# 
# ![Wheat Field with Cypresses](images/vangogh.jpg)
# 
# 
# 
# 

# ###### Link
# ```markdown
# [Attribution](https://www.metmuseum.org/art/collection/search/436535)
# ```
# Vincent van Gogh / Public domain
# The Metropolitan Museum of Art, New York - Purchase, The Annenberg Foundation Gift, 1993 - 
# [Attribution](https://www.metmuseum.org/art/collection/search/436535)

# ###### Bullet List
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

# ###### Numbered List
# ```markdown
# 1. I am a
#   1. numbered
# 1. list
# ```
# 1. I am a
#   1. numbered
# 1. list

# ###### LaTeX
# ```markdown
# $$e=mc^2$$
# ```
# 
# 
# $$e=mc^2$$

# ###### Blockquotes
# ```markdown
# > This is a blockquote.
# ```
# > This is a blockquote.

# ##### Code

# Cells can be run using the Run button &#9658; or selecting one of the run options under the Run menu. 
# 
# Try this out! You can change what is in the cell and rerun the same cell, which is useful for debugging.

# In[2]:


2 + 2 


# **Your turn**: In a new cell, figure out what **5315 + 5618** is. 

# In[3]:


## remove and type out 5315 + 5618
## then hit the play button


# #### Jupyter ✨ MAGIC ✨

# When using other languages in Jupyter/JupyterLab, we need to designate the cell we are using with this langauge or function. To "activate" these language, we need to use ✨ MAGIC ✨. Here are a couple of examples.

# ##### HTML

# In[4]:


get_ipython().run_cell_magic('html', '', '<ol>\n  <li>apple</li>\n  <li>banana</li>\n  <li>cookies</li>\n</ol>')


# ##### R Language

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


# ##### SQL

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


# More information can be found here: [Jupyter ✨ MAGIC ✨](https://ipython.readthedocs.io/en/stable/interactive/magics.html)

# ## All About Google Colab - 🐦

# ### Working with Data 
# For this notebook, we will be focusing on using Google Colab {cite:ps}`GoogleColaboratoryIO`
# 

# #### A Temporary Solution
# 
# You can create and interact with files when you access Google Colab, *BUT* they will disappear after your session ends. An example would be:

# In[9]:


f = open("thanosSnapping.txt", "a")
f.write("you should've gone for the head")
f.close()


# ```{warning} 
# Super serious here. 
# If files are not written to your local machine or your Google Drive. They will be **gone** the next time you log in.
# ```

# We need a better solution for this. So, let's take a look at these options. 

# #### Connecting to Your Google Drive
# 
# There are two ways to connect to your Google Drive. 
# 
# ##### Selecting the Icon to Connect
# 
# ```{image} https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/connectToDrive.PNG
# :alt: Icon for Connecting to Google Colab
# :width: 400px
# :align: center
# ```
# 
# ##### Connecting Using Google Colab Code
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

# ##### I am Connected, Now What?
# 
# It can be a bit difficult to figure out where to place files and where your files are located in Google Colab. Once you connect, you will need to navigate the folder structure to find your file. They did not make this very easy to find. Here is a quick screenshot.
# 
# 
# ```{image} https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/contentFolder.PNG
# :alt: file structure in Google Colab
# :width: 400px
# :align: center
# ```

# #### Connecting to Gitlab
# Another way to work with data outside of your Google Drive is using something like GitHub or, in our case GitLab. A bit of a warning before we begin.

# ```{warning}
# Github is an open repository. Any file placed on Github is available for *ANYONE* to view, download, or edit. 
# ```

# Make sure you read of the terms of services as well! 
# 
# For accessing GitLab through Penn State, here is the link (https://git.psu.edu/). You do need to setup a username/password to start creating. 
# 
# If you are interest in using Git, let me show the basics. 
# 
# ##### Creating a Connection (SSH)
# 
# The first step in this process is to create a connection between Google Colab and GitLab, and this starts with saying to Google Colab: You can connect to this resource because I gave you access. The way we do this is to create an *SSH Key*.
# 
# 

# ```{note}
# Code will run in Google Colab but has been commented out to work on the website. 
# ```

# ```python
# !ssh-keygen -t ed25519 -C "SSH key for google colab"
# ```

# In[10]:


#!ssh-keygen -t ed25519 -C "SSH key for google colab"


# To see this file, we will need to read the file using a UNIX command call 😸 (cat or con**cat**enate)
# 
# ```python 
# !cat /root/.ssh/id_ed25519.pub
# ```

# In[11]:


#!cat /root/.ssh/id_ed25519.pub


# We now need to tell SSH that the PSU GitLab is fine to connect to (it is a known host). 
# 
# ```python
# !ssh-keyscan git.psu.edu >> /root/.ssh/known_hosts
# ```

# In[12]:


#!ssh-keyscan git.psu.edu >> /root/.ssh/known_hosts


# Now in GitLab, we need to add this SSH key to our account. 
# 
# ![GitLab adding SSH](https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/gitlabSSH.PNG)

# Finally, let's test this connection. 
# 
# ```python
# !ssh -T git@git.psu.edu
# ```

# In[13]:


#!ssh -T git@git.psu.edu


# You should receive a message that looks like this:
# >Warning: Permanently added the ECDSA host key for IP address '***.***.***.***' to the list of known hosts.
# Welcome to GitLab, @you!

# ##### The Push and Pull of Git

# Git, basically, is a push and pull mechanism. You *pull* your project down from GitLab. Make changes. Then *push* it back to GitLab. Here is an example of doing this with your file from before. First, we **clone** the repository. 
# 
# ```python
# !git clone git@git.psu.edu:pmd19/workshop_temp.git
# ```

# In[14]:


#!git clone git@git.psu.edu:pmd19/workshop_temp.git


# We then **pull** the current content from GitLab. Note cd stands for Change Directory, and PWD stands for Print Work Directory. 
# 
# ```python
# %cd /content/workshop_temp
# !pwd
# !git pull origin master
# ```

# In[15]:


#%cd /content/workshop_temp
#!pwd
#!git pull origin master


# We write our file to our directory and **add** it to the list of things we want to update on GitLab.
# 
# ```python
# !pwd
# f = open("thanosSnapping.txt", "w")
# f.write("you should've gone for the head")
# f.close()
# !git add "thanosSnapping.txt"
# ```

# In[16]:


#!pwd
#f = open("thanosSnapping.txt", "w")
#f.write("you should've gone for the head")
#f.close()
#!git add "thanosSnapping.txt"


# Git wants to make sure it knows who is updating what, so it needs a person and an email address to associate the changes. We then **commit** to these changes, and finally, we **push** our changes to GitLab.
# 
# ```python
# !git config --global user.email 'pmd19@psu.edu'
# !git config --global user.name 'Patrick Dudas'
# !git commit -m "testing"
# !git push git@git.psu.edu:pmd19/workshop_temp.git
# ```

# In[17]:


#!git config --global user.email 'pmd19@psu.edu'
#!git config --global user.name 'Patrick Dudas'
#!git commit -m "testing"
#!git push git@git.psu.edu:pmd19/workshop_temp.git

