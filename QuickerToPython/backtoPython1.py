#backtoPython1.py
# In this programm we will be going through
# python language on a fast track basis

#type(1)           -> <class 'int'>
#type("hello")     -> <class 'str'>
#type(None)        -> <class 'NoneType'>


#bool is a subtype of int , where True==1 and False=0
# s= 'Arthur'
# s[2]=='t'
# s[-1]=='r'
# s[:2]=='Ar'
# s[1:-1]=='rthu'
# s[1:5:2]=='rh'
# s[::-1]=='ruhtrA'
# loops

# range(3)   generates -> 0,1,2
# range(5,10) generates -> 5,6,7,8,9
# range(2,15,3) generates ->2,5,8,11



#***************************************************

# writing function
 
#  def function (param1, param2):
#     value= do_something()
#     return value
#    return is optional, implicitly returns None



#*****************************************************
# objects

# everything is an object
# isinstance(4, object)              => True
# isinstance("helloworld", object)   => True
# isinstance(None, object)           => True
# isinstance([1,2,4],object)         => True




#****************************************************
# OBJECT IDENTITY

# id(object)      ++++> gives object's identity
# objects are tagged with their type at runtime
# objects containg pointers to their data  blob
# this means even small things take pa a lot of space
# (4).__sizeOf__()                  ==> 28(Bytes)

#****************************************************
# variables 

# variables are references to objects 
# little more than a pointer


#***************************************************
#Symbol Table
# python namespace maintains information about labels
# local namespace (via locals()), global , module , and more!

#***************************************************
# Variable Assignment

# assigning from a variable does not copy an 
# instead it adds another referecne to the same object
# python will always handle the creationg of new objects



#****************************************************

#Duck Typing

# promotes interface-style generic programming
# eg 
# compute(a, b,c)
# return (a+b)*c

# compute(1,2,3)             ==> 9
# compute([1],[2,3], 2)      ==> [1,2,3,1,2,3]
# compute('l','olo',4)       ==> 'lololololo'

# for compute all that matters is that the arguments support + and * 


#*****************************************************
# is vs ==:
#----------------------------------
# We've seen == for equality testing
# 1 == 1.0
# but we know these are different in some fundamental way
# type(1) != type(1.0)
# is vs ==
# True!
# int != float
# The "is" operator checks identity instead of equality
# when comparing against None or other singletons,
# always use "is" None instead of "== " None

# "is" checks if the suitcases are the same
# "=="" checks if they have the same stuff inside

# Use "=="" when comparing values
# Use "is" when comparing identities
#****************************************************

# Special characters:
# --------------------------------
# print('"Yes," he said.')       # => "Yes," he said.
# print("\"Yes,\" he said.")     # => "Yes," he said.



#***************************************************
# Useful String Methods:
# ---------------------------
# greeting="Hello World! "
# greeting[4]                    # => 'o'
# 'world' in greeting            # => True
# len(greeting)                  # => 13
# greeting.find('lo')  		   # => 3 (-1 if not found)
# greeting.replace('llo', 'y')   # => "hey world!"
# greeting.startswith('hell')    # => True
# greeting.isalpha()             # => False (due to '!')
# greeting.lower() 			   # => "hello world! "
# greeting.title() 			   # => "Hello World! "
# greeting.strip()               # => "Hello world!"   (space got stripped)
# greeting.strip('! ')           # => "Hello world" (no '!')


#****************************************************
# Strings <—> Lists:
# ---------------------------------
# # `split` partitions a string by a delimiter
# 'ham cheese bacon'.split()            # => ['ham', 'cheese', 'bacon']

# '03-30-2016'.split(sep='-')           # => ['03', '30', '2016']

# # `join` creates a string from a list

# ', '.join(['Eric', 'John', 'Michael']) # => "Eric, John, Michael


#*****************************************************
# STRING FORMATTING:
# ----------------------------------
# # Curly braces in strings are placeholders
# '{} {}'.format('monty', 'python')      # => 'monty python'

# # Provide values by position or by placeholder

# "{0} can be {1} {0}s".format("strings", "formatted")

# "{name} loves {food}".format(name="Sam", food="plums")

# # Pro: Values are converted to strings

# "{} squared is {}".format(5, 5 ** 2)

# # Padding is just another specifier
# '{:10}'.format('hi')                  # => 'hi '
# '{:^12}'.format('TEST')               # => '****TEST****

# # You can even look up values!
#  captains = ['Kirk', 'Picard']
# "{caps[0]} > {caps[1]}".format(caps=captains)

# # Pure C-style formatting
# "%s, %s, %s. (Act %d)" % ('Words', 'words', 'words', 2)   #=> Words, words, words. (Act 2)

# using  .format() is the fastest and most convenient


#******************************************************

# FILE I/O:
# ---------------------------------------
# WHAT IF 

# f = open('file.txt', 'r')
# print(1 / 0)                  # Crash!
# f.close()
# this file is never closed 

# (use)

# [ 
# with open('file.txt', 'r') as f:
# content = f.read()
# print(1/0)
# ]
# f.closed                       # => True

# | The with expr as var construct                |
# | ensures that expr will be entered and exited  |
# | regardless of the code block execution        |

#*********************************************************
# SCRIPTS, MODULES, IMPORTS

# scripts:


# """ File: hello.py """
# def greet(name):
# print("Hey {}, I'm Python!".format(name))



# # Run only if called as a script

# if __name__ == '__main__':
# name = input("What is your name? ")
# greet(name)

# The special __name__ variable is set to
# '__main__' if your file is executed as a script