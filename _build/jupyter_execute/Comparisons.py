#!/usr/bin/env python
# coding: utf-8

# # Comparison Operators

# We need to be able to compare different variables.  We will be working on:
# * Are these things the same?
# * Are these things not the same?
# * How do these things compare?
# 
# We can compare any data type, and our output will be a boolean (True or False).  The other things we will cover are:
# * Comparing different data types
# * Making multiple comparisons at once
# 
# Comparison operators are important on their own (how do these things compare?) and are also useful for sorting and switching (see the next notebook.) 

# ## Are these things the same?

# We have already initiated variables by setting something equal to something else - let's do that here by setting aVar equal to 10 and then setting bVar equal to aVar.

# In[1]:


aVar = 10
bVar = aVar
cVar = 11 

print( "aVar=", aVar, "; bVar =", bVar, "; cVar = ", cVar )


# The first comparison operator is '==' which tests to see if two variables are equal. 

# In[2]:


print( "aVar=", aVar, "; bVar =", bVar, "; cVar = ", cVar )

# Is aVar equal to bVar?
print( "\n#-# Is aVar equal to bVar?")
print( aVar == bVar )

# Is aVar equal to cVar?
print( "\n#-# Is aVar equal to cVar?")
print( aVar == cVar )


# This tells us that aVar is equal to bVar, because it returns 'True' and aVar is not equal to cVar, as that returns 'False.'

# We can also do comparisons with other variable types.  Here's an example with strings instead of integers

# In[3]:


aStr = 'apple'
bStr = 'banana'
cStr = 'apple' 
print( "aStr=", aStr,"; bStr =", bStr,"; cStr = ", cStr )

# Is aStr equal to bStr?
print( "\n#-# Is aStr equal to bStr?")
print( aStr == bStr )

# Is aStr equal to cStr?
print( "\n#-# Is aStr equal to cStr?")
print( aStr == cStr )


# ## Are these things different?

# We can also test to see if two values are not equal using the '!=' operator.

# In[4]:


print( "aVar=", aVar, "; bVar =", bVar, "; cVar = ", cVar )

# Is aVar not equal to bVar?
print( "\n#-# Is aVar not equal to bVar?")
print( aVar != bVar )

# Is aVar not equal to cVar?
print( "\n#-# Is aVar not equal to cVar?")
print( aVar != cVar )


# This gives us the opposite of what we had before.  It is false that aVar and bVar are not equal, meaning that they are equal.  It is true that aVar and cVar are not equal.

# ## How do these things compare?

# We can also compare the magnitude of values using '<', '<=', '>'and '>=', which will return 'True' if the condition is being met.

# In[5]:


print( "aVar=", aVar, "; bVar =", bVar )

# Is aVar less than bVar?
print( "\n#-# Is aVar less than bVar?")
print( aVar < bVar )

# Is aVar less than or equal to bVar?
print( "\n#-# Is aVar less than or equal to bVar?")
print( aVar <= bVar )

# Is aVar greater than or equal to bVar?
print( "\n#-# Is aVar greater than or equal to bVar?")
print( aVar >= bVar )

# Is aVar greater than bVar?
print( "\n#-# Is aVar greater than bVar?")
print( aVar > bVar )


# ## Warnings for variable types

# We do have to watch out for our types. A string of a value is not the same as a value

# In[6]:


aStr = '10'
aFlt = 10.0
print( "aVar=", aVar, "; aStr =", aStr, "; aFlt =", aFlt  )

# Is aVar equal to aStr?
print( "\n#-# Is aVar equal to aStr?")
print( aVar == aStr )
print( "aVar type is ", type( aVar ), "; and aStr type is ", type( aStr ) )

# Is aVar equal to aFlt?
print( "\n#-# Is aVar equal to aFlt?")
print( aVar == aFlt)


# We can compare integers and floats (!) but not other disparate data types.
# 
# If you let python take care of your data-types, be warned that they could be different from what you think they are!

# ## Multiple Comparisons

# We can make multiple comparisons at once by stringing the statements
# * and
# * not
# * or
# 
# together. 
# 
# The individual testable (true/false) components need to be broken apart. For example,
# * If the V CATA bus is coming around the corner, then I need to run towards the bus stop
# 
# requires several things for it to be true, and to require running.  We can break these things out with:
# * If there is a vehicle coming around the corner AND that vehicle is a CATA bus AND that CATA bus is a V, then I need to run towards the bus stop
# 
# We will only run towards the bus stop if all of the statements are true

# ### AND

# The and operator will return True if all of the conditions are met

# In[7]:


print( "aVar=", aVar, "; bVar =", bVar, "; cVar = ", cVar )

# Is aVar equal to 10?
print( "\n#-# Is aVar equal to 10?")
print( aVar == 10 )
      
# Is aVar equal to bVar?
print( "\n#-# Is aVar equal to bVar?" )
print( aVar == bVar )

# Is aVar equal to cVar?
print( "\n#-# Is aVar equal to cVar?" )
print( aVar == cVar )

# Is aVar equal to 10 AND aVar equal to bVar?
print ( "\n#-# Is aVar equal to 10 AND aVar equal to bVar?")
print( (aVar == 10) and (aVar == bVar) )

# Is aVar equal to 10 AND aVar equal to cVar?
print ( "\n#-# Is aVar equal to 10 AND aVar equal to cVar?")
print( (aVar == 10) and (aVar == cVar) )


# We can also string as many comparisons together as we want

# In[8]:


print( (1 < 2) and (1 < 3) and (1 < 4) and (1 < 5) and (1 < 6) and (1 < 7) and (1 < 8) )


# ### OR

# If we want 'True' for either of the conditions to be met, we can use the 'or' operator.

# In[9]:


print( "aVar=", aVar, "; bVar =", bVar, "; cVar = ", cVar )

# Is aVar equal to 10?
print( "\n#-# Is aVar equal to 10?")
print( aVar == 10 )
      
# Is aVar equal to bVar?
print( "\n#-# Is aVar equal to bVar?" )
print( aVar == bVar )

# Is aVar equal to cVar?
print( "\n#-# Is aVar equal to cVar?" )
print( aVar == cVar )

# Is aVar equal to 10?
print( "\n#-# Is aVar equal to 11?")
print( aVar == 11 )

# Is aVar equal to 10 OR aVar equal to bVar?
print ( "\n#-# Is aVar equal to 10 OR aVar equal to bVar?")
print( (aVar == 10) or (aVar == bVar) )

# Is aVar equal to 10 OR aVar equal to cVar?
print ( "\n#-# Is aVar equal to 10 or aVar equal to cVar?")
print( (aVar == 10) or (aVar == cVar) )

# Is aVar equal to 11 OR aVar equal to cVar?
print ( "\n#-# Is aVar equal to 11 or aVar equal to cVar?")
print( (aVar == 11) or (aVar == cVar) )


# ### Not

# We can add a not to change the meaning of the and/or operators

# In[10]:


print( "aVar=", aVar, "; bVar =", bVar )

# Is aVar equal to 10?
print( "\n#-# Is aVar equal to 10?")
print( aVar == 10 )
      
# Is aVar equal to bVar?
print( "\n#-# Is aVar equal to bVar?" )
print( aVar == bVar )


# Is aVar equal to 10 AND aVar equal to bVar?
print ( "\n#-# Is aVar equal to 10 AND aVar equal to bVar?")
print( (aVar == 10) and (aVar == bVar) )

# Is aVar equal to 10 AND NOT aVar equal to bVar?
print ( "\n#-# Is aVar equal to 10 AND NOT aVar equal to bVar?")
print( (aVar == 10) and not (aVar == bVar) )


# ## Check yourself

# Try to fill in code to fulfill the request!  Here are some variables used in the excercise

# In[11]:


dogA_color='brown'
dogA_mass=42
dogA_gender='male'
dogA_age=5
dogA_name='chip'

dogB_color='white'
dogB_mass=19
dogB_gender='female'
dogB_age=2
dogB_name='lady'


# Is dogA the same color as dogB? (False)

# In[12]:


# Example:
print( dogA_color == dogB_color )


# Does dogA have the same name as dogB? (False)

# In[13]:


# Try it out here:


# Is dogA older than dogB? (True)

# In[14]:


# Try it out here:


# Is dogA the same gender as dogB? (False)

# In[15]:


# Try it out here:


# Is dogA heavier than dogB and have a different name than dogB? (True)

# In[16]:


# Try it out here:


# Does dogA have a different age than dogB and not a different gender than dogB? (False)

# In[17]:


# Try it out here:


# In[ ]:




