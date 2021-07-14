#!/usr/bin/env python
# coding: utf-8

# # Creating a Function

# In[1]:


## Functions


# Functions allow us to do repeated tasks easily by writing the code only once.  Functions will have a name, inputs and outputs and can be called anywhere the task is repeated.
# 
# There are functions that are built in to python, for example we have already been using the type() function, which tells us the type of variable we are using.  Note that print is also a function!

# In[2]:


aVal = 10.0
print( type( aVal ) )


# Functions have four typical parts:
# * Name - what you call your function
# * Input arguments - what you provide
# * Outputs - what the function gives back
# * Math/Magic - what the function does

# In python, we use def to define a function with the function name and inputs followed by a colon.  The python function is then separated from the rest of the code by a tab. Some languages use braces rather than indentation.
# ````python
# def functionName( inputs ):
#     # Operate on the inputs
#     ouputs = inputs + 5
#     # Return what we want to back
#     return outputs;
#    ````

# Let's look at an example function, which changes degrees Farenheit to Celsius. 

# In[3]:


def changeFromFToC( farVal ):
    # Change the temperature from Farenheit to Celsius
    cVal = (farVal - 32.0) * 5.0 / 9.0
    return cVal 


# Here, our function name is changeFromFToC, the input is farVal, the temperature in Farenheit, the output is cVal, and the temperature in Celsius. We can print or store the output from the function.  Note that the function has to be defined before we use it - the cell with the function definition has to have run before we can call the function.

# In[4]:


# Change 14 deg F to Celsius
print( "#-# 14 Deg Farenheit in Celsius" )
print( changeFromFToC( 14 ) )

# Change from 68 deg F to Celsius
print( "\n#-# 68 Deg Farenheit in Celsius" )
niceTempC = changeFromFToC( 68 )
print( niceTempC )


# ### Multiple inputs and outputs

# In[5]:


def changeFromFToCAndK( farVal ):
    # Change the temperature from Farenheit to Celsius and Kelvin
    cVal = (farVal - 32.0) * 5.0 / 9.0
    kVal= cVal + 273.15
    return cVal, kVal    
    
# Change 14 deg F to Celsius and Kelvin
print( "#-# 14 Deg Farenheit in Celsius and Kelvin" )
print( changeFromFToCAndK( 14 ) )

# Change 212 deg F to Celsius and Kelvin
print( "\n#-# 212 Deg Farenheit in Celsius and Kelvin" )
boilingC, boilingK = changeFromFToCAndK( 212 ) 
print( boilingC )
print( boilingK )

# Change 32 deg F to Celsius and Kelvin
print( "\n#-# 32 Deg Farenheit in Celsius and Kelvin" )
freezing = changeFromFToCAndK( 32 ) 
print( freezing[0] )
print( freezing[1] )


# In[6]:


def windChillFar( tempF, windMPH ):
    # Calculate the wind chill index using
    # tempF: Temperature in Farenheit
    # windMPH: Wind in miles per hour
    # to return the wind chill index
    return 35.74 + (0.6215 * tempF) - (35.75 * windMPH**.16) + (0.4275 * tempF * windMPH**.16)

print( "#-# Wind chill at 32 with 8 mph wind" )
print( windChillFar( 32, 8 ) )


# ### Functions calling other functions

# Functions can call other functions.  Here we add three using a function to add two and then adding one.

# In[7]:


def addTwo( inValAddTwo ):
    # Add two to the input
    return inValAddTwo + 2

def addThree( inValAddThree ):
    # Add three two the input
    return addTwo( inValAddThree ) + 1

# Add three to four
print( "#-# Add three to four using addThree, which calls addTwo" )
print( addThree( 4 ) )


# Functions can also call themselves - these are called recursive functions.  See how we calculate the factorial by subtracting one and calling the function again. 

# In[8]:


def factorialRecursive( facIn ):
    # Calculate the factorial
    if facIn == 1:
        return facIn
    else:
        return facIn * factorialRecursive( facIn - 1)

# Use a recursive function to calculate the factorial of 5
print( "\n#-# Use a recursive function to calculate the factorial of 5" )
print( factorialRecursive( 5 ) )


# ### The gotcha for functions: Where variables can be used

# The biggest gotcha on functions is with variable scope: 
# * Variables defined in a function are not accessible from the outside
# * Functions have access to more than just the variables passed in

# In[9]:


# Function to add four
def addFour( inValAddFour ):
    middleVal = addTwo( inValAddFour )
    finalAns = addTwo( middleVal )
    print( "#-# Print from In Function" )
    print( "startingVal = ", startingVal )
    print( "middleVal = ", middleVal )
    print( "finalAns = ", finalAns )
    return finalAns
    
#-#-#-#-#-#-#
# Not in the function - this is what runs
startingVal = 10

# Call the function using startingVal as the input parameter
fourAdded = addFour( startingVal )

# Print out some things
print( "\n#-# Print after the function" )
print( "startingVal = ", startingVal )
print( "fourAdded = " , fourAdded )

# This won't work because middleVal was only defined within the function
print( "middleVal = ", middleVal )

