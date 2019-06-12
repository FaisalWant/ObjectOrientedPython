# backtoPython4.

# List Comprehension vs. Map+filter
# Memory---
#    ---------------------------------------------------- 
#  | List Comprehensions: buffer all computed results    |
#  | Map/Filter: only compute output elements when asked |
#   ----------------------------------------------------
# Map:
# ----------
# map(fn, iter)
# same as :

# [len(s) for s in languages]

# The map() function applies a given function 
# to each item of an iterable and returns 
# a list of the result
# e.g:

# numbers = (1, 2, 3, 4)
# result = map(calculateSquare, numbers)
# print(result)

# lambda with map:   lambda ---->>  [Function on Fly]
# ------------------------
# numbers = (1, 2, 3, 4)
# result = map(lambda x: x*x, numbers)
# print(result

# FILTER:
# ----------
# The filter() method returns an "iterator" that passed the   [ Filter returns just an itertor ]
# function check for each element in the iterable

# same as :
#-------------
# [element for element in iterable if predicate(element)]
# e.g
#  #list of alphabets
# alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# # function that filters vowels

# def filterVowels(alphabet):
#     vowels = ['a', 'e', 'i', 'o', 'u']

#     if(alphabet in vowels):
#         return True
#     else:
#         return False

# filteredVowels = filter(filterVowels, alphabets)

# print('The filtered vowels are:')
# for vowel in filteredVowels:
#     print(vowel)                         # The filtered vowels are: a,e,i,o




# LAMBDA:
# ----------------------------
# triple = lambda x: x * 3 # NEVER EVER DO THIS

# # Squares from 0**2 to 9**2
# map(lambda val: val ** 2, range(10))

# # Tuples with positive second elements
# filter(lambda pair: pair[1] > 0, [(4,1), (3, -2), (8,0)]
# ------------------------
#    ITERABLES:           |
# ----------------------
# ------------------------------
# # Build an iterator over [1,2,3]
# it = iter([1,2,3])
# next(it) # => 1
# next(it) # => 2
# next(it) # => 3
# next(it) # raises StopIteration error

# ------------------------------
# GENERATOR:                   |
# ------------------------------

# Return an iterator that generates
# a stream of values

# E.G:
# def generate_ints(n):
#    for i in range(n):
#      yield i

# g = generate_ints(3)
# type(g) # => <class 'generator'>
# next(g) # => 0
# next(g) # => 1
# next(g) # => 2
# next(g) # raises StopIteration

# DECORATORS:
# --------------------------------
# functions as argument and functions as return values
# add functionality to an existing code.
# Also called metaprogramming as a part of the program tries to modify another part of the program at compile time.
# Functions can be passed as arguments to another function.
# e.g:

# def debug(function):           --> here debug is the decorator function
#    def wrapper(*args, **kwargs):
#        print("Arguments:", args, kwargs)
#        return function(*args, **kwargs)
#    return wrapper


# @debug
# def foo(a, b, c=1):
# return (a + b) * c    --> is equivalent to def foo(a,b, c=1):
#                                               return (a+b)*c
#                                                 foo=debug(foo)

# NOTE:
# add chaining decorators here

# OOP in PYTHON:
# ----------------------
# Entering a class definition creates a new "namespace"-ish
# Really, a special __dict__ attribute where others live
# Exiting a class definition creates a class object


# class Complex:
# def __init__(self, realpart=0, imagpart=0):
# self.real = realpart
# self.imag = imagpart

# # Make an instance object `c`!
# c = Complex(3.0, -4.5)

# c.real, c.imag                              # => (3.0, -4.5)

# Custom Constructor using __init__:
# -----------------------------------
# Class instantiation calls the special method __init__ if it exists

# You can't overload __init__! Use keyword arguments or factory methods

# Attribute references first search the instance's __dict__ attribute, then the class object's

# SETTING DATA ATTRIBUTE:
# -----------------------
# # You can set attributes on instance (and class) objects
# # on the fly (we used this in the constructor!)
# c.counter = 1
# while c.counter < 10:
# c.counter = x.counter * 2
# print(c.counter)
# del c.counter # Leaves no trace

# # prints 1, 2, 4, 8

# Setting attributes actually inserts into the instance object's __dict__ attribute

# CALLING METHODS:
# ----------------------------
# class MyClass:

# """A simple example class"""
# num = 12345
# def greet(self):
# return "Hello world!


# ............................................
# x = MyClass()
# x.greet()                          # 'Hello world!'
#                                    # Weird... doesn't `greet` accept an argument?
# print(type(x.greet))               # method
# print(type(MyClass.greet))         # function
# print(x.num is MyClass.num)        # True
# print(x.greet is MyClass.greet)    # False

# A method is a function bound to an object
# method ≈ (object, function

# Methods calls invoke special semantics
# object.method(arguments) = function(object, arguments)

# class Pizza:

# 	def __init__(self, radius, toppings, slices=8):
# 		self.radius = radius
# 		self.toppings = toppings
# 		self.slices_left = slices

# 	def eat_slice(self):
# 		if self.slices_left > 0:
# 		self.slices_left -= 1
# 		else:
# 		print("Oh no! Out of pizza")

# 	def __repr__(self):

# 		return '{}" pizza'.format(self.radius)


# p = Pizza(14, ("Pepperoni", "Olives"), slices=12)

# print(Pizza.eat_slice)                # => <function Pizza.eat_slice>

# print(p.eat_slice)                    # => <bound method Pizza.eat_slice of 14" Pizza>

# method = p.eat_slice

# method.__self__                       # => 14" Pizza

# method.__func__                       # => <function Pizza.eat_slice>

# p.eat_slice()                         # Implicitly calls Pizza.eat_slice(p)


# CASES TO CONSIDER:
# ---------------------------------
# class Dog:
# # Let's try a default argument!
# def __init__(self, name='', tricks=[]):
# 	self.name = name
# 	self.tricks = tricks
# def add_trick(self, trick):
# 	self.tricks.append(trick)
# ...................................
# d = Dog('Fido')
# e = Dog('Buddy')
# d.add_trick('roll over')
# e.add_trick('play dead')
# d.tricks                             # => ['roll over', 'play dead'] (shared value)

# ----------
# [solution]
# ----------
# class Dog:
# 	def __init__(self, name):
# 		self.name = name
# 		self.tricks = []        # New list for each dog
# 	def add_trick(self, trick):
# 		self.tricks.append(trick)
# d = Dog('Fido')
# e = Dog('Buddy')
# d.add_trick('roll over')
# e.add_trick('play dead')
# d.tricks                         # => ['roll over']
# e.tricks                         # => ['play dead']


# CONVENTIONS:
# -------------------
# A method's first parameter should always be self
# Why? 
# Explicitly differentiate instance and local variables

# Method calls already provide the calling object as the first argument to the class function

# Attribute names prefixed with a leading underscore are intended to be private (e.g. _spam)

# Use verbs for methods and nouns for data attributes


# INHERITANCE:
# ----------------------
# class DerivedClassName(BaseClassName):
#  pass

# FACTS ABOUT SINGLE INHERITANCE:
# ----------------------------------
# A class object 'remembers' its base class

# Python 3 class objects inherit from object (by default)

# Method and attribute lookup begins in the derived class

# Proceeds down the chain of base classes

# Derived methods override (shadow) base methods

# Like `virtual` in C++

# MULTIPLE INHERITANCE:
# ------------------------------------
# class Derived(Base1, Base2, …, BaseN):
#    pass
#    order matters, base classes are separted by commas

# Attribute lookup is (almost) depth-first, left-to-right

# Officially, "C3 superclass linearization" (Wikipedia)

# Class objects have a (hidden) function attribute .mro()

# Shows linearization of base classes

# ATTRIBUTE RESOLUTION:
# -------------------------------------
# class A: pass
# class B: pass
# class C: pass
# class D: pass
# class E: pass
# class K1(A, B, C): pass
# class K2(D, B, E): pass
# class K3(D, A): pass
# class Z(K1, K2, K3): pass

# Z.mro()                              # [Z, K1, K2, K3, D, A, B, C, E, object]


# MAGIC METHODS:
# ------------------------

# class MagicClass:
# 	def __init__(self): ...
# 	def __contains__(self, key): ...
# 	def __add__(self, other): ...
# 	def __iter__(self): ...
# 	def __next__(self): ...
# 	def __getitem__(self, key): ...
# 	def __len__(self): ...
# 	def __lt__(self, other): ...
# 	def __eq__(self, other): ...
# 	def __str__(self): ...
# 	def __repr__(self): ... # And even more
# .....................................

# x = MagicClass()
# y = MagicClass()
# str(x)          						# => x.__str__()
# x == y 									# => x.__eq__(y)
# x < y 									# => x.__lt__(y)
# x + y 									# => x.__add__(y)
# iter(x) 								# => x.__iter__()
# next(x) 								# => x.__next__()
# len(x) 									# => x.__len__()
# el in x 								# => x.__contains__(el)


# BaseException
# ├── SystemExit
# ├── KeyboardInterrupt
# ├── GeneratorExit
# └── Exception
# ├── StopIteration
# ├── ArithmeticError
# │ ├── FloatingPointError
# │ ├── OverflowError
# │ └── ZeroDivisionError
# ├── AssertionError
# ├── AttributeError
# ├── BufferError
# ├── EOFError
# ├── ImportError
# ├── LookupError
# │ ├── IndexError
# │ └── KeyError
# ├── MemoryError
# ├── NameError
# │ └── UnboundLocalError
# ├── OSError




# # This is what enables us to use with ... as ...
# with open(filename) as f:
# 	raw = f.read()

# # is (almost) equivalent to

# 	f = open(filename)
# 	f.__enter__()
# 	try:
# 	   raw = f.read()
# 	finally:
# 	   f.__exit__() # Closes the file