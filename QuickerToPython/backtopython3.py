# backtopython3.py

# FUNCTIONS:
# ------------------------
# All functions return some value
# Even if that value is None
# No return statement or just return implicitly returns None
#  -------------------------   
# |Returning multiple values|
#  -------------------------
# 
# You can use a tuple! In some cases, use a namedtuple
# return value1, value2, value3

# LOCAL FUNCTION SCOPE:
# -------------------------

# x = 2
# def foo(y):
# z = 5
# print(locals())
# print(globals()['x'])
# print(x, y, z)
# foo(3)          # prints {'y': 3, 'z': 5}
#                 # print 2
#                 # prints 2, 3, 5


#  ---------------------------
# | DEFAULT/ NAMED PARAMETERS:
#  ---------------------------
# Usually used to provide "settings" for the function.

# ask_yn(prompt, retries=4, complaint='...')

# # Call with only the mandatory argument
# ask_yn('Really quit?')
# # Call with one keyword argument
# ask_yn('OK to overwrite the file?', retries=2)
# # Call with one keyword argument - in any order!
# ask_yn('Update status?', complaint='Just Y/N')




# RULES ABOUT FUNCTION CALLS:
# --------------------------------

# Keyword arguments must follow positional arguments
# All keyword arguments must identify some parameter
# Even positional ones
# No parameter may receive a value more than once




# Variadic Positional Arguments:
# -------------------------------
# A parameter of form " *args "  captures excess positional args
# These excess arguments are bundled into an args tuple
# Why?
# Call functions with any number of positional arguments
# Capture all arguments to forward to another handler
# Used in subclasses, proxies, and decorators
# e.g

# # Suppose we want a product function that works as so:
# product(3, 5)                               # => 15
# product(3, 4, 2)                            # => 24
# product(3, 5, scale=10)                     # => 150

# # product accepts any number of arguments

# def product(*nums, scale=1):
# 	p = scale
#     for n in nums:
#       p *= n
#     return p


# UNPACKING Variadic POSITIONAL ARUGMENTS:
# -----------------------------------------------
# # Suppose we want to find 2 * 3 * 5 * 7 * … up to 100
# def is_prime(n): pass # Some implementation
# # Extract all the primes
# primes = [number for number in range(2, 100)
# if is_prime(number)]
# # primes == [2, 3, 5, …]
# print(product(*primes)) # equiv. to product(2, 3, 5, …)


#  ----------------------------------------
# |VARIADIC KEYWORD ARGUMENTS:             |  
# -----------------------------------------
# A parameter of the form **kwargs captures all excess keyword
# arguments
# These excess arguments are bundled into a kwargs dict
# Why?

# Allow arbitrary named parameters, *** usually for configuration ***
# Similar: capture all arguments to forward to another handler
# Used in subclasses, proxies, and decorators

# def authorize(quote, **speaker_info):

# print(">", quote)

# print("-" * (len(quote) + 2))

# for k, v in speaker_info.items():      ## accessing the variadic positional arguments
#   print(k, v, sep=': ')

# |****************************|
# |speaker_info = {            |  
# |'act': 1,                   |
# |'scene': 1,                 |
# |'speaker': "Duke Orsino",   |
# |'playwright': "Shakespeare" |
# |}                           |
# ******************************



# UNPACKING VARIADIC KEYWORD ARGUMENTS:
# -------------------------------------
# local symbol table
# {
# 'x': 3,
# 'foo': 'fighter',
# 'y': 4,
# 'bar': 'bell',
# 'z': 5, …
# }

# print("{z}^2 = {x}^2 + {y}^2".format(x=x, y=y, z=z))
# print("{z}^2 = {x}^2 + {y}^2".format(**locals()))  # Equivalent to .format(x=3, foo='fighter', y=4, ...)