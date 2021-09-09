#!/usr/bin/env python
# coding: utf-8

# # All About Google Colab - 🐦

# ## Working with Data 
# For this notebook, we will be focusing on using Google Colab {cite:ps}`GoogleColaboratoryIO`
# 

# ### A Temporary Solution
# 
# You can create and interact with files when you access Google Colab, *BUT* they will disappear after your session ends. An example would be:

# In[1]:


f = open("thanosSnapping.txt", "a")
f.write("you should've gone for the head")
f.close()


# ```{warning} 
# Super serious here. 
# If files are not written to your local machine or your Google Drive. They will be **gone** the next time you log in.
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
# It can be a bit difficult to figure out where to place files and where your files are located in Google Colab. Once you connect, you will need to navigate the folder structure to find your file. They did not make this very easy to find. Here is a quick screenshot.
# 
# 
# ```{image} https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/contentFolder.PNG
# :alt: file structure in Google Colab
# :width: 400px
# :align: center
# ```

# ### Connecting to Gitlab
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
# #### Creating a Connection (SSH)
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

# In[2]:


#!ssh-keygen -t ed25519 -C "SSH key for google colab"


# To see this file, we will need to read the file using a UNIX command call 😸 (cat or con**cat**enate)
# 
# ```python 
# !cat /root/.ssh/id_ed25519.pub
# ```

# In[3]:


#!cat /root/.ssh/id_ed25519.pub


# We now need to tell SSH that the PSU GitLab is fine to connect to (it is a known host). 
# 
# ```python
# !ssh-keyscan git.psu.edu >> /root/.ssh/known_hosts
# ```

# In[4]:


#!ssh-keyscan git.psu.edu >> /root/.ssh/known_hosts


# Now in GitLab, we need to add this SSH key to our account. 
# 
# ![GitLab adding SSH](https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/gitlabSSH.PNG)

# Finally, let's test this connection. 
# 
# ```python
# !ssh -T git@git.psu.edu
# ```

# In[5]:


#!ssh -T git@git.psu.edu


# You should receive a message that looks like this:
# >Warning: Permanently added the ECDSA host key for IP address '***.***.***.***' to the list of known hosts.
# Welcome to GitLab, @you!

# #### The Push and Pull of Git

# Git, basically, is a push and pull mechanism. You *pull* your project down from GitLab. Make changes. Then *push* it back to GitLab. Here is an example of doing this with your file from before. First, we **clone** the repository. 
# 
# ```python
# !git clone git@git.psu.edu:pmd19/workshop_temp.git
# ```

# In[6]:


#!git clone git@git.psu.edu:pmd19/workshop_temp.git


# We then **pull** the current content from GitLab. Note cd stands for Change Directory, and PWD stands for Print Work Directory. 
# 
# ```python
# %cd /content/workshop_temp
# !pwd
# !git pull origin master
# ```

# In[7]:


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

# In[8]:


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

# In[9]:


#!git config --global user.email 'pmd19@psu.edu'
#!git config --global user.name 'Patrick Dudas'
#!git commit -m "testing"
#!git push git@git.psu.edu:pmd19/workshop_temp.git

