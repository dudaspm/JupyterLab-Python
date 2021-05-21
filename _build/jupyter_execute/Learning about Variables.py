#!/usr/bin/env python
# coding: utf-8

# # What is a variable?

# When we are developing our idea, we sometime need to use values multiple times or change the value based on our code. This is where variables become very helpful. Let's look at an example.
# 
# In this example, we are adding a few numbers togethers. In this instance, if all we care about is getting the result (similar to a calculator). Then variables are not needed. 

# In[1]:


5 + 3 + 16


# But let's look an example where we need to get the circumference of a circle using multiple radii. The equation for the circumference of a circle is: $C = 2 \pi r$

# Let's say the radius is 5

# In[2]:


2 * 3.14159265359 * 5


# OK, how about radius 10 and 11 and 4 and ... 
# Well in this, we might not want to rewrite 3.14159265359 over and over. So, in this case, we want to create a variable for this and we will call it pi. 

# In[3]:


pi = 3.14159265359


# Now, every time we reference the variable called **pi** it will refer to the number **3.14159265359**
# 
# Let's try those radii again (10, 11, 4)

# In[4]:


2 * pi * 10


# In[5]:


2 * pi * 11


# In[6]:


2 * pi * 4


# By the way, if you happen to get an error:
# ```javascript
# NameError: name 'pi' is not defined
# ```
# Make sure you go to the cell that has
# ```python
# pi = 3.14159265359
# ```
# and run this cell *first* then try the other calculations. 

# ## Type of Variables

# There are multiple types of variables. The most common (and the ones we will talk about) are:
# 
# * Integers (whole numbers)
# * Float (Floating points or numbers with a decimal)
# * Text
# * Lists
# * Dictionaries
# 
# The nice thing about Python is that we do **not** need to specify (or declare) which type we are using. Python will figure this out for us! 
# 
# BUT FIRST, a quick detour...
# 
# We need to talk about Camel Casing.

# ### Camel Case

# <img src="https://upload.wikimedia.org/wikipedia/commons/c/c8/CamelCase_new.svg" alt="camel case" width="100" style="float:right"/>
# Variable names must be one continous string of letters/numbers. So, let's say we wanted to create a variable called "number of kittens." Instead calling this variable <em>number of kittens</em>, I would call it <em>numberOfKittens</em>. Why the capitalization? because it makes it easier to separate out the words in the name. As in, <em>numberofkittens</em> vs. <em>numberOfKittens</em>. We have a fun name for this: camel case. 

# <cite>File:CamelCase new.svg. (2020, April 15). Wikimedia Commons, the free media repository. Retrieved 15:25, June 3, 2020 from https://commons.wikimedia.org/w/index.php?title=File:CamelCase_new.svg&oldid=411544943.</cite>

# ### Integers or int

# As mentioned, integers are whole numbers. Let's create an example. How about we use our numberOfKittens. We will then set this value to 0. As in, we have 0 kittens.

# In[7]:


numberOfKittens = 0


# One thing we might want to do is to have Python tell us what **type** this variable is. Well Python has a function for this called
# 
# ```python
# type()
# ```

# In[8]:


type( numberOfKittens )


# So this checks out, we made an int and it is showing us we have an int.
# 
# Now, once we have a variable, it is not static. We can change the value as much as we need to. Running the next cell will continually add 10 to our original variable. 
# 
# Try running this a few times.

# In[9]:


numberOfKittens = numberOfKittens + 10
numberOfKittens


# In[10]:


from IPython.display import Markdown as md
md(f"**or**<br />in more human-readable terms. <br />numberOfKittens (new value {numberOfKittens})  = numberOfKittens (originally {numberOfKittens-10}) + 10<br />numberOfKittens is now {numberOfKittens}<br />**or**")


# In[11]:


from IPython.display import HTML as html
listOfCats = []
for i in range(numberOfKittens): 
    listOfCats.append("🐈")
   
display(html(' '.join([str(elem) for elem in listOfCats])))


# ### Floats

# Floats are similar to integers, but with more precision.
# Float comes from Floating point or a number with a decimal point. 
# 
# This example starts at 0, but note that this is .0 
# Adding the decimal tells Python that we should have a float value instead of an interger. 

# In[12]:


aFloatVariable = .0


# Let's again, check the variable type. 

# In[13]:


type( aFloatVariable )


# Looks good. 
# 
# And again, we will add 10 to this. There is something specific interesting here, see if you spot it.

# aFloatVariable = aFloatVariable + 10
# aFloatVariable

# If you guessed "mixing a float and interger," you got it. Let's see an example. 

# #### Mixing integers and floats

# In Python (3, more specifically), the variable will always take the form of the most precision. So, by default, a float.

# In[14]:


letsSeeWhatHappens = numberOfKittens + aFloatVariable
letsSeeWhatHappens


# We can force variables to be a certain type. We call this 'type-cast' and can be used to:
# 
# * make an integer into a float
# * a float to an integer
# * an integer to a string (we have not discussed this yet)
# * a float to a string (we have not discussed this yet)
# * etc...

# #### type-cast

# ```{note}
# type-cast is temporary. If you do not use a type-cast, the variable will revert back to its original variable type. 
# ```

# Let's switch our numberOfKittens to a float using 
# ```python
# float()
# ```
# 
# and turn our aFloatVariable to an integer using
# 
# ```python
# int()
# ```

# In[15]:


float(numberOfKittens)


# In[16]:


int(aFloatVariable)


# ```{admonition} Common Question
# :class: tip
# What happens when you convert a float like .5 to an integer? Does it round up or down?
# ```

# Well let's see what happens.

# In[17]:


printList = []
for i in range(10): printList.append("for value %s we will get %s" % ((i/10),int(i/10)))

display(md('<br />'.join([str(elem) for elem in printList])))


# So, in conclusion. It will always round down.

# ### Strings

# Strings are sequence of letters, numbers, and special characters 

# In[18]:


helloStatement = "hello everyone!"


# In[19]:


print( type( helloStatement ), helloStatement )


# In[20]:


singleCharacter = "a"
print( singleCharacter, type( singleCharacter ) )


# #### String Indexing/String Slicing

# In[21]:


print( helloStatement[1] )


# In[22]:


print( helloStatement[0:5] )


# In[23]:


print( helloStatement[:5] )


# In[24]:


print( helloStatement[5:] )


# #### String functions

# In[25]:


################
## Find
################
print( helloStatement.find("one") )
print( helloStatement.find("me") )
print( helloStatement.capitalize() )
print( helloStatement.lower() )
print( helloStatement.split(" ") )


# What will this do?

# In[26]:


print( helloStatement.capitalize().lower() )
# We can chain these!
print( helloStatement[:5].capitalize() )


# #### Concatenating Strings

# In[27]:


courseName = "bio"
courseNumber = "101"
print( courseName+courseNumber )
print( "%s%s" % (courseName,courseNumber) )


# Why I like to use %s

# In[28]:


variable1 = "variable1"
variable2 = "variable2"
variable3 = "variable3"
variable4 = "variable4"
variable5 = "variable5"
print( variable1 + "," + variable2 + "," + variable3 + "," + variable4 + "," + variable5 )
print( "%s,%s,%s,%s,%s" % (variable1,variable2,variable3,variable4,variable5) )


# In[29]:


# let's concatenate the strings
courseNameNumber = "%s%s" % (courseName,courseNumber)
print( courseNameNumber )
print( "I am currently sitting in %s" % (courseNameNumber) )


# ### Booleans

# Booleans are used to do comparisions (true/false), (1/0), (yes/no)

# In[30]:


someCondition = True
type( someCondition )


# In[31]:


# Will come back to this in a second (==)
(someCondition == False)


# In[32]:


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

# In[33]:


groceryList = ["apple", "banana", "eggs"]
print( groceryList )


# In[34]:


# or another way
groceryList = []
groceryList.append("apple")
groceryList.append("banana")
groceryList.append("eggs")
print( groceryList )


# We can access each entry by using an index number (**remember starts at 0**)

# In[35]:


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




