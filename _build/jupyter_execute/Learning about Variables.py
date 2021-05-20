#!/usr/bin/env python
# coding: utf-8

# # What is a variable?

# Variables are used to store values
# 
# In Python, we do not need to declare what type of variable is being used. Python does this for us!

# ### Integers

# In[1]:


someInteger = 0


# In[2]:


type( someInteger )


# In[3]:


someInteger = someInteger + 10
print( someInteger )


# In[4]:


print( type( someInteger ), someInteger )


# ### Floats

# Floats are similar to integers, but with more precision.
# Float comes from Floating point. 

# In[5]:


someFloat = .0
print( type( someFloat ), someFloat )


# In[6]:


someFloat = someFloat + 10
print( type( someFloat ), someFloat ) 


# #### Mixing integers and floats

# In[7]:


print( someInteger + someFloat )
print( someInteger + 1.1 )
print( someInteger, (someInteger/3) )
# Why does this happen?  Integer math can create floats!
# This isn't the case in python 2.x: Integer / Integer = Integer
# You can introduce a float to make the answer a float in python 2.x
print( someInteger, (someInteger/3.) )


# #### type-cast

# In[8]:


print( someInteger, someFloat )
print( float( someInteger ), int( someFloat ) )
print( someInteger, (float( someInteger )/3) )


# ### Strings

# Strings are sequence of letters, numbers, and special characters 

# In[9]:


helloStatement = "hello everyone!"


# In[10]:


print( type( helloStatement ), helloStatement )


# In[11]:


singleCharacter = "a"
print( singleCharacter, type( singleCharacter ) )


# #### String Indexing/String Slicing

# In[12]:


print( helloStatement[1] )


# In[13]:


print( helloStatement[0:5] )


# In[14]:


print( helloStatement[:5] )


# In[15]:


print( helloStatement[5:] )


# #### String functions

# In[16]:


################
## Find
################
print( helloStatement.find("one") )
print( helloStatement.find("me") )
print( helloStatement.capitalize() )
print( helloStatement.lower() )
print( helloStatement.split(" ") )


# What will this do?

# In[17]:


print( helloStatement.capitalize().lower() )
# We can chain these!
print( helloStatement[:5].capitalize() )


# #### Concatenating Strings

# In[18]:


courseName = "bio"
courseNumber = "101"
print( courseName+courseNumber )
print( "%s%s" % (courseName,courseNumber) )


# Why I like to use %s

# In[19]:


variable1 = "variable1"
variable2 = "variable2"
variable3 = "variable3"
variable4 = "variable4"
variable5 = "variable5"
print( variable1 + "," + variable2 + "," + variable3 + "," + variable4 + "," + variable5 )
print( "%s,%s,%s,%s,%s" % (variable1,variable2,variable3,variable4,variable5) )


# In[20]:


# let's concatenate the strings
courseNameNumber = "%s%s" % (courseName,courseNumber)
print( courseNameNumber )
print( "I am currently sitting in %s" % (courseNameNumber) )


# ### Booleans

# Booleans are used to do comparisions (true/false), (1/0), (yes/no)

# In[21]:


someCondition = True
type( someCondition )


# In[22]:


# Will come back to this in a second (==)
(someCondition == False)


# In[23]:


if (False): 
    print( "yes for False!" )
if (True): 
    print( "yes for True!" )


# if (0): 
#     print "yes for 0!"
# if (1): 
#     print "yes for 1!"

# ### Lists

# Lists (or also known as Arrays) are exactly that. A list of data. Exmaple:

# In[24]:


groceryList = ["apple", "banana", "eggs"]
print( groceryList )


# In[25]:


# or another way
groceryList = []
groceryList.append("apple")
groceryList.append("banana")
groceryList.append("eggs")
print( groceryList )


# We can access each entry by using an index number (**remember starts at 0**)

# In[26]:


print( groceryList[2] )
print( groceryList[0] )
print( groceryList[1] )
print( groceryList[3] )


# To do this more efficiently, we will be using loops (for and while, we will talk about later).

# ### Dictionary

# Dictionaries are used to index based on a specific key. As in:
# 
# dictionary[\"street adddress\" (key)] = "123 Apple St." (value)

# In[ ]:


personalInformation = {}
personalInformation["streetAddress"] = "123 Apple St."
personalInformation["firstName"] = "Patrick"
personalInformation["lastName"] = "Dudas"
print( personalInformation )


# Note the order.

# Again, to do this more efficiently, we will be using loops (for and while, we will talk about later).

# In[ ]:




