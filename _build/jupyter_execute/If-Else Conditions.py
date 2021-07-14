#!/usr/bin/env python
# coding: utf-8

# # If-Else Conditions

# We can condition our data using if-else statements and switch cases.  If-else statements allow us to do different things if a certain criterion is met or not. We can count the odds and evens in our someNumbers list.

# ## if

# The *if* statement starts with if and then lists a condition that may or may not be met. If the condition is true, we do what is listed. If it is not, we move on. 
# 
# Our example here is straightforward, if answer is greater than 30, print something.

# In[1]:


answer = 42

if answer > 30:
    print( "This number is greater than 30")


# OK, same concept. 

# In[2]:


answer = 42

if answer > 50:
    print( "This number is greater than 50")


# ```{note}
# Note the structure of a Python if/else statement. Where some languages use { } to denote the start and end of the if/else statement. Python uses spaces. 
# 
# if (condition): <-colon
#  <- space or tab
#  
# Anything that is also spaced or tab is *part* of the if statement. 
# 
# ```

# ### Where the if Starts and Ends

# As mentioned in our note, the if/else statement uses space

# ## else

# In these examples, only the numbers that are greater than 30 and 50 will get any response.  We can add a response for values that do not meet the conditional statement found within the if using an else statement

# In[3]:


answer = 42

if answer > 30:
    print( "This number is greater than 30")
else:
    print( "This number is not greater than 30")
    
if answer > 50:
    print( "This number is greater than 50")
else:
    print( "This number is not greater than 50")


# ## elif (else if)

# If-else statements can also be stacked together, to allow for additional sorting using multiple conditions.  The way this is done in python is by using 
# ```python
# elif
# ```
# to provide another condition. Let's count the odds again, and count the evens but split between those that are greater than or equal to 0 and those that aren't, and change all of the negative evens to 0.  Note that we use the index of the value so that we can set the value to 0 for the negative evens.
