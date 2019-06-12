# backtoPython2.py

# DATASTRUCTURES
# Lists
# Dictionaries
# Tuples
# Sets
# Advanced Looping
# Comprehensions


# Lists:
# Finite, ordered, mutable
# sequence of elements
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# # Lists can contain elements of different types
# mixed = [4, 5, "seconds"]

# # Append elements to the end of a list

# numbers.append(7) # numbers == [2, 3, 5, 7]
# numbers.append(11) # numbers == [2, 3, 5, 7, 11]

# # Lists really can contain anything - even other lists!

# x = [letters, numbers]

# x                          # => [['a', 'b', 'c', 'd'], [2, 3, 5, 7, 11]]

# list methods:
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# # Extend list by appending elements from the iterable
# my_list.extend(iterable)

# # Insert object before index
# my_list.insert(index, object)

# # Remove first occurrence of value, or raise ValueError
# my_list.remove(value)

# # Remove all items
# my_list.clear()

# # Return number of occurrences of value
# my_list.count(value)

# # Return first index of value, or raise ValueError
# my_list.index(value, [start, [stop]])

# # Remove, return item at index (def. last) or IndexError
# my_list.pop([index])

# # Stable sort *in place*
# my_list.sort(key=None, reverse=False)

# # Reverse *in place*.
# my_list.reverse()

# General Queries on Iterables:
# -----------------------------------------

# # Length (len)
# len([]) 						# => 0
# len("python") 					# => 6
# len([4,5,"seconds"]) 			# => 3

# # Membership (in)
# 0 in []  						# => False
# 'y' in 'python' 				# => True
# 'minutes' in [4, 5, 'seconds']  # => False

# DICTONARIES:
# --------------------------------------------
# Mutable map from hashable values to arbitrary objects

# empty = {}
# type(empty) 					# => dict

# empty == dict() 				# => True
# a = dict(one=1, two=2, three=3)

# b = {"one": 1, "two": 2, "three": 3}

# a == b 							# => True

# ACCESS AND MUTATE:
# ---------------------------------------------

# b = {"one": 1, "two": 2, "three": 3}
# # Get

# d['one'] # => 1
# d['five'] # raises KeyError

# # Set

# d['two'] = 22 # Modify an existing key
# d['four'] = 4 # Add a new key

# d = {"CS":[106, 107, 110], "MATH": [51, 113]}
# d["COMPSCI"] # raises KeyError
# ------------------------------------------
# |Use get() method to avoid the KeyError  |
# ------------------------------------------


# d.get("CS") # => [106, 107, 110]
# d.get("PHIL") # => None (not a KeyError!)

# Delete:
# ---------
# d = {"one": 1, "two": 2, "three": 3}
# 1) del d["one"]       ->Raises KeyError if invalid key

# 2) d.pop("three", default) # => 3 remove and return d['three'] or default value if not int the map

# 3) d.popitem() # => ("two", 2) remove and return and aribtrary (key, value) pair, Useful for destructive iteration

# d = {"one": 1, "two": 2, "three": 3}
# d.keys()
# d.values()
# d.items()


# Common Dict Operations:
# -----------------------------------------
# len(d)

# key in d # equiv. to `key in d.keys()`

# value in d.values()

# d.copy()

# d.clear()

# for key in d: # equiv. to `for key in d.keys():`
# print(key)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# Tuples :
#|--------------------|
# immutable Sequence
# Store collections of heterogeneous data
# Tuples can be dictionary keys, but lists cannot

# fish = (1, 2, "red", "blue")
# fish[0] # => 1
# fish[0] = 7 # Raises a TypeError   you cannot change any element in a tuple


# Argument packing and Unpacking:
# ---------------------------------------

# t = 12345, 54321, 'hello!'     --> Comma-separated Rvalues are converted to a tuple
# print(t) # (12345, 54321, 'hello!')
# type(t) # => tuple 

# x, y, z = t                   --> Comma-separated L values are unpacked automatically

# x # => 12345
# y # => 54321
# z # => 'hello

# Swapping Values:
# ---------------------------
# x=5            x=6
# y=6   want     y=5

# |XOR magic|
# x= x^y
# y=x^y
# x=x^y
# print(x, y)                     # => 6 5

# |tuple packing|

#  x,y=y,x  
# print(x,y)                      #=> 6,5


# SETS:
# ------------------------------

# Unordered collection of
# distinct hashable elements

# Fast membership testing
# O(1) vs. O(n)

# empty_set = set()
# set_from_list = set([1, 2, 1, 4, 3]) # => {1, 3, 4, 2}

# basket = {"apple", "orange", "apple", "pear", "banana"}
# len(basket)                          # => 4
# "orange" in basket                   # => True
# "crabgrass" in basket                # => False


# a = set("mississippi") # {'i', 'm', 'p', 's'}
# a.add('r')
# a.remove('m') # raises KeyError if 'm' is not present
# a.discard('x') # same as remove, except no error

# a.pop() # => 's' (or 'i' or 'p')
# a.clear()
# a = set("abracadabra") # {'a', 'r', 'b', 'c', 'd'}
# b = set("alacazam") # {'a', 'm', 'c', 'l', 'z'}

# # Set difference
# a - b                      # => {'r', 'd', 'b'}
# # Union
# a | b                      # => {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
# # Intersection
# a & b                      # => {'a', 'c'}

# # Symmetric Difference

# a ^ b                      # => {'r', 'd', 'b', 'm', 'z', 'l'}




# ReWriting is_efficient:
# ----------------------------------------
# EFFICIENT_LETTERS = "BCDGIJLMNOPSUVWZ"
# def is_efficient(word):
# for letter in word:
# if letter not in EFFICIENT_LETTERS:
# return False
# return True




# using sets:
# ----------------------------------------


# EFFICIENT_LETTERS = set("BCDGIJLMNOPSUVWZ")
# def is_efficient(word):
# return set(word) <= EFFICIENT_LETTERS
# =====================================
# ______




# |zip:|
# ------
# questions = ['name', 'quest', 'favorite color']
# answers = ['Lancelot', 'To seek the holy grail', 'Blue']
# for q, a in zip(questions, answers):
# print('What is your {0}? {1}.'.format(q, a))

# The zip() function generates pairs of entries
# from its arguments



# REVERSE ITERATION:
# -----------------------
# for i in reversed(range(1,10,2)):
# print(i, end=',')



# SORTED ITERATION:
# -----------------------
# basket = ['pear', 'banana', 'orange', 'pear', 'apple']
# for fruit in sorted(basket):
# print(fruit)




# LIST COMPREHENSION:
# -----------------------
# [f(xs) for xs in iter if pred(xs)]




# DISTIONARY COMPREHENSION:
# -----------------------
# {key_func(vars):val_func(vars) for vars in iterable}
# e.g
# {v:k for k, v in d.items()}



# SET COMPREHENSION:
# -------------------------
# {func(vars) for vars in iterable}
# {word for word in hamlet if is_palindrome(word.lower())}
