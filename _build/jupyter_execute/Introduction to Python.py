#!/usr/bin/env python
# coding: utf-8

# # Introduction to Python

# In this section I wanted to introduce a few basic concepts and give an outline of this section. 

# ## Comments in Python

# In Python, we can creat comments in the code itself. Considering we can use markdown langauge (as you see here 😁), we won't be using this too much in this notebook. Though, here is an example. 
# 
# Basically, you use the... umm... hashtag? number sign? pound sign? 
# 
# This thing -> #

# In[1]:


# I am a comment in Python
# Here is 2 + 2
2 + 2
# As you can see, these are not "computed" using Python. 
# We are just comments for the person looking at this.
# Or... you!


# ## Print Function

# We will being using...
# 
# ```python
# print()
# ```
# 
# ...several times in this notebook. 
# 
# Basically, it is a function to print out strings, variables, numbers, functions, etc. 
# 
# Let's use the classic example.

# In[2]:


print( "hello, world!" )


# OR

# In[3]:


print("hello, world!")


# ## Help Function

# The...
# 
# ```python
# help()
# ```
# 
# ... function is exactly what it is. It is a function to 🌟 help 🌟 you understand the basic usage of another function. 

# In[4]:


help(print)


# ## Resources

# Highly suggest looking for answers using [StackOverflow](https://stackoverflow.com/help/searching)

# ## Common Errors

# One of the most common errors in Python is the dreaded 
# 
# ```python
# 2 + 2
#  3 + 3
# 
#   File "<ipython-input-1-0dcc020fd5cb>", line 2
#     3 + 3
#     ^
# IndentationError: unexpected indent
# ```
# 
# Why does this occur? Well because Python uses spacing or tabs to distinquish where things like loops, functions, and if/else statements start and end. So, if you add an extra space or tab at the beginning of the statement, you will see this message. If you do, check your spacing. 

# ```{note}
# Python can get weird with issue. As you can, technically, start code wherever. As long as you are consistent. The next cell shows an example of this... oddity.
# 
# ```

# In[5]:


2+2
3+3


# still works! 

# In[ ]:




