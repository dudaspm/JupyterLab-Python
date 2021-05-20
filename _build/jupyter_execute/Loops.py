#!/usr/bin/env python
# coding: utf-8

# # Introduction to Functions, Loops and Sorting

# One of the features of programming is that we have many options to do the same tasking multiple times.  The three methods we will be looking at are:
# * Functions
# * For loops
# * While Loops
# 
# We will also look at two different methods for sorting or conditioning data:
# * if-else statements
# * switch statements

# ## Functions

# Functions allow us to do repeated tasks easily by writing the code only once.  Functions will have a name, inputs and outputs and can be called anywhere the task is repeated.
# 
# There are functions that are built in to python, for example we have already been using the type() function, which tells us the type of variable we are using.  Note that print is also a function!

# In[1]:


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

# In[2]:


def changeFromFToC( farVal ):
    # Change the temperature from Farenheit to Celsius
    cVal = (farVal - 32.0) * 5.0 / 9.0
    return cVal 


# Here, our function name is changeFromFToC, the input is farVal, the temperature in Farenheit, the output is cVal, and the temperature in Celsius. We can print or store the output from the function.  Note that the function has to be defined before we use it - the cell with the function definition has to have run before we can call the function.

# In[3]:


# Change 14 deg F to Celsius
print( "#-# 14 Deg Farenheit in Celsius" )
print( changeFromFToC( 14 ) )

# Change from 68 deg F to Celsius
print( "\n#-# 68 Deg Farenheit in Celsius" )
niceTempC = changeFromFToC( 68 )
print( niceTempC )


# ### Multiple inputs and outputs

# Functions can also have multiple inputs and outputs.  The example below changes Farenheit to Celsius and Kelvin.  We can take the outputs individually, or as a list.  You have to either have the same number of outputs as is provided, or just one for a list.

# In[4]:


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


# The example function below to calculate the wind chill uses two inputs and only calculates the returned value.

# In[5]:


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

# In[6]:


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

# In[7]:


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

# In[8]:


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


# ## For Loops

# Loops allow us to do the same thing to each item in a list or array. One of the most basic types of loops is a for loop - this allows us to iterate over any sequence.
# 
# We set up a for loop using 2 things:
# * loop variable - the value of the sequence currently being used
# * sequence - the data we iterate over
# 
# The sequence can be any list.  We set up for loop using the for and in keywords, a colon, and all of the code within the for loop indented

# In[11]:


exampleList = ['a', 'niner', 6, 6.1, 'V@@@', 1001/2, 42]

# Print the whole list
print( "#-# Print the whole list" )
print( exampleList )

# Use a for loop to print the individual values in the list
print( "\n#-# Use a for loop to print the individual values in the list" )
for loopVar in exampleList:
    print( loopVar )


# Sometimes, it's helpful to iterate using indices.  For example, linear algebra heavy calculations will almost always use indices to make working with vectors and matrices easier.
# 
# We can use the len() and range() functions to show the length and create indices.  We can then iterate using the indices, rather than the values.  Here we loop through the same someNumbers list using spot, the index.

# In[12]:


someNumbers = [ -3, -2, -1, 0, 1, 2, 3 ] 

# Print out our variables:
print( "exampleList = ", exampleList )
print( "someNumbers = ", someNumbers )

# Loop through using the index
for spot in range( len( someNumbers ) ):
    print( "Spot = ", spot, "; exampleList[spot] = ", exampleList[spot], "; someNumbers[spot] = ", someNumbers[spot] )


# You may have noticed that the second line is indented.  This is how we indicate what is in the loop.  Our loop can have many lines (all indented).  The first line that isn't indented indicates we are out of the loop.  This is the python syntax for in and out of the loop; other coding languages use other things such as braces {}.  Note that blank lines don't matter, just indentation.

# In[13]:


for val in someNumbers:
    print( "val = ", val )
    
    print( "Inside the loop" )
print( "#-# Outside the loop #-#" )


# ## While loops

# For loops are used when you have something you are iterating over - you know the length.  You can use a while loop if you don't know the number of times something will run. The while loop code requires a conditinal statement; the loop will continue to run as long as this is true and will not run again as soon as it is false.

# #### Conceptual Example
# You can think about taking a test in two different ways:
# 
# For loop:
# ```python
# for problem in test:
#     "solve problem"
#     ```
# 
# While loop:
# ```python 
# while percentDone < (100):
#     "increase percentDone"
# ```

# The condition being set by the while statement will cause this to run as long as the statement is true

# In[14]:


answer = 'up'
print( "#-# answer = ", answer )
print( "Is answer equal to up? = ", answer == 'up' )

while answer == 'up':
    print( "\nIn the while loop now" )
    print( "LOOP 1st: Is answer equal to up? = ", answer == 'up' )
    answer = 'down'
    print( "LOOP 2nd: Is answer equal to up? = ", answer == 'up' )

print( "\n#-# answer = ", answer ) 
print( "Is answer equal to up? = ", answer == 'up' )


# One thing to note is that the while loop won't ever be entered if the condition is false when the statement 

# In[15]:


answer = 'up'
print( "#-# answer = ", answer )
print( "Is answer equal to down? = ", answer == 'down' )

while answer == 'down':
    print( "\nIn the while loop now" )
    print( "LOOP 1st: Is answer equal to up? = ", answer == 'up' )
    answer = 'down'
    print( "LOOP 2nd: Is answer equal to up? = ", answer == 'up' )

print( "\n#-# answer = ", answer ) 
print( "Is answer equal to down? = ", answer == 'down' )


# Let's set up a while loop to find the first number from our someNumbers that meets some criterion - for example the first number that is greater than 1.5.
# 
# We need to initialize our criterion variable to 0 and set up an iterator to count up for us.

# In[16]:


pushToLarge = 0
counter = 0
print( "#-# Initialization" )
print( "counter = ", counter, "pushToLarge = ", pushToLarge)

while pushToLarge < 1.5:
    print( "\n#-# Loop" )
    pushToLarge = someNumbers[counter]
    print( "counter = ", counter, "pushToLarge = ", pushToLarge)
    counter = counter + 1

print( "\n#-# Final" )
print( pushToLarge )


# While loops will keep iterating as long as the statement stays true.  Infinite loops are caused by a condition that always stays true.  Use the stop button (black square) to stop this errorneous code, which will never stop after uncommenting. 

# In[17]:


# Uncomment all the lines below and run if you want an infinite loop to run
#counter = 1
#while counter > 0:
#    counter = counter + 1
#    print( counter )


# ## Conditioning Data

# We can condition our data using if-else statements and switch cases.  If-else statements allow us to do different things if a certain criterion is met or not. We can count the odds and evens in our someNumbers list.

# ### If-Else Statements

# The if statement starts with if and then lists a condition that may or may not be met. If the condition is true, we do what is listed.  If it is not, we move on. 

# In[18]:


answer = 42

if answer > 30:
    print( "This number is greater than 30")
    
if answer > 50:
    print( "This number is greater than 50")


# In these examples, only the numbers that are greater than 30 and 50 will get any response.  We can add a response for values that do not meet the conditional statement found within the if using an else statement

# In[19]:


answer = 42

if answer > 30:
    print( "This number is greater than 30")
else:
    print( "This number is not greater than 30")
    
if answer > 50:
    print( "This number is greater than 50")
else:
    print( "This number is not greater than 50")


# Here's a more complicated example.  We count the number of odd and even values in someNumbers by using an if-else statement to separate the odds (which have a remainder or modulo of 1 when divided by 2) from the evens.

# In[23]:


someNumbers = [ -3, -2, -1, 0, 1, 2, 3 ] 
print( "someNumbers = ", someNumbers )

# Initialize the number of odd and even numbers
odds = 0
evens = 0

# Loop through someNumbers and increment odds and evens
for val in someNumbers:
    print( val, (val%2) == 1 )
    if (val%2) == 1:
        # Increment the odds by one if val/2 has a remainder of 1
        odds = odds + 1
        print( val, " is odd!" )
    else:
        # Increment the evens by one if val/2 doesn't have a remainder of 1
        evens = evens + 1
        
# Print out some info at the end        
print( "\n#-# For loop is done")
print( "odds = ", odds )
print( "evens = ", evens )


# If-else statements can also be stacked together, to allow for additional sorting using multiple conditions.  The way this is done in python is by using 
# ```python
# elif
# ```
# to provide another condition. Let's count the odds again, and count the evens but split between those that are greater than or equal to 0 and those that aren't, and change all of the negative evens to 0.  Note that we use the index of the value so that we can set the value to 0 for the negative evens.

# In[25]:


someNumbers = [ -3, -2, -1, 0, 1, 2, 3 ] 
print( "someNumbers = ", someNumbers )
# Initialize the number of odd and even numbers
odds = 0
posEvens = 0
negEvens = 0

# Loop through someNumbers and increment odds and evens
for spot in range(len(someNumbers)):
    if (someNumbers[spot]%2) == (1):
        # Increment the odds by one if val/2 has a remainder of 1
        odds = odds + 1
    elif (someNumbers[spot]) >= (0):
        # Increment the evens by one if val/2 doesn't have a remainder of 1 and is greater than or equal to 0
        posEvens = posEvens + 1
    else:
        # Increment the evens by one if val/2 doesn't have a remainder of 1 and is greater than or equal to 0
        negEvens = negEvens + 1
        someNumbers[spot] = 0
        
# Print out some info at the end        
print( "\n#-# For loop is done")
print( "odds = ", odds )
print( "posEvens = ", posEvens )
print( "negEvens = ", negEvens )
print( "someNumbers = ", someNumbers )


# Note: we don't need a final else if we don't care about values that don't meet our earlier criteria.  Here, we skip the final else, doing nothing if the even number is less than or equal to 0.

# In[26]:


print( "someNumbers = ", someNumbers )
# Initialize the number of odd and positive even numbers
odds = 0
posEvens = 0

# Loop through someNumbers and increment odds and positive evens
for spot in range(len(someNumbers)):
    if (someNumbers[spot]%2) == (1):
        # Increment the odds by one if val/2 has a remainder of 1
        odds = odds + 1
    elif (someNumbers[spot]) > (0):
        # Increment the evens by one if val/2 doesn't have a remainder of 1 and is greater than 0
        posEvens = posEvens + 1
        
# Print out some info at the end        
print( "\n#-# For loop is done")
print( "odds = ", odds )
print( "posEvens = ", posEvens )


# ### Switch Cases

# Switch Cases are specialized if-else statements - the criteria must be met exactly. Let's work on an example that changes between month numbers and month names. We first set up a dictionary that will be used for the evaulation.  We will use numbers as the keys and use the abbreviations as the values. 

# In[27]:


monthSwap = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}


# We then can use a get statement with the key to find the result:
# ```python
# result = monthSwap.get(key, 'default')
# ```
# The value listed in default is returned if the given key isn't present.

# In[28]:


print( "monthSwap = ", monthSwap)

# Print out the 5th month
print( "\n#-# Key = 5")
print( monthSwap.get(5,"oooooops!") )

# Print out the 19th month
print( "\n#-# Key = 19")
print( monthSwap.get(19,"oooooops!") )


# Let's use our dictionairy to print out some birthdays, given the day, month and year in numerical format.  Note that we use the get function of the dictionary, which has error checking, and then gather the same info without get and the error checking.

# In[29]:


birthdayMonths = [4,2,11,9,15]
birthdayDays = [6,12,24,23,15]
birthdayYears = [1955,1983,1999,2010,2015]

# Cycle through all of the birthdays and print out 
for spot in range(len(birthdayDays)):
    print ( "\n#-# Spot = ", spot )
    # Print using get, which has built in error checking
    print( monthSwap.get(birthdayMonths[spot],"oooooops!"), birthdayDays[spot], birthdayYears[spot] )
    # Print without get, which gives an error if passed a key that doesn't exist
    print( monthSwap[birthdayMonths[spot]], birthdayDays[spot], birthdayYears[spot] )


# You can build the same sort of code with if, elif, and else statements, but it takes a lot more coding. 

# In[30]:


for spot in range(len(birthdayDays)):
    if (birthdayMonths[spot]) == (1):
        mon = 'Jan'
    elif (birthdayMonths[spot]) == (2):
        mon = 'Feb'
    elif (birthdayMonths[spot]) == (3):
        mon = 'Mar'
    elif (birthdayMonths[spot]) == (4):
        mon = 'Apr'
    elif (birthdayMonths[spot]) == (5):
        mon = 'May'
    elif (birthdayMonths[spot]) == (6):
        mon = 'Jun'
    elif (birthdayMonths[spot]) == (7):
        mon ='July'
    elif (birthdayMonths[spot]) == (8):
        mon = 'Aug'
    elif (birthdayMonths[spot]) == (9):
        mon = 'Sep'
    elif (birthdayMonths[spot]) == (10):
        mon = 'Oct'
    elif (birthdayMonths[spot]) == (11):
        mon = 'Nov'
    elif (birthdayMonths[spot]) == (12):
        mon = 'Dec'
    else:
        mon = 'oooooops!'
        
    # Print statements
    print ( "\n#-# Spot = ", spot )
    print ( mon, birthdayDays[spot], birthdayYears[spot] )


# You'll note that the first term, April, needs to check itself 4 times before returning an answer, versus the one operation using the key with the dictionary

# ## Check yourself

# Try to fill in code to fulfill the request!  Here is a variable used in the excercises

# In[155]:


aListOfNumbers = [6, 3, 4, 5, 7, 8, 9 ]


# Write a function that returns the length of aListOfNumbers as well as the maximum value. Hint: max() is a built in function

# In[156]:


# Try it here:


# Use a for loop to add up all of the numbers in aListOfNumbers.

# In[157]:


# Try it here:


# Use a while loop to find the first number in aListOfNumbers that is both greater than 5 and a multiple of 4.

# In[158]:


# Try it here:


# Count the number of values in aListOfNumbers that are:
# * even
# * odd and divisible by three
# * odd and not divisible by three
# 
# using if, elif and else.

# In[159]:


# Try it here:


# Create a dictionary with keys 1-8 corresponding to the words one, two, three, etc. Loop through aListofNumbers to print out the word corresponding to the digit and provide a default value of 'Not Found' if the key is not contained within the dictionary.  You should get: six three four five seven eight Not Found

# In[160]:


# Try it here:


# In[ ]:




