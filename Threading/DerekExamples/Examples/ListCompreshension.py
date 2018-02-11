


# Generate a list of 10 values a

# Multiply them by 2 

# Return mulitiple of 8

#print([ x for x in [ i*2 for i in range(10)] if x %8==0])



# Problem 

# Generate a list of 50 random values between 1 and 1000
# and return those that are mulitiples of 9
# you'll have to use a list comprehension in a list comprehension


# import random

# print([x for x in [ random.randint(1,1001)  for i in range(1,51)] if x%9==0])

# # multidimensional List

# multiList= [[1,2,3],
#             [4,5,6],
#             [7,8,9]
#             ]

# print([col[1] for col in multiList])


# Generators


def isprime(num):
    for i in range(2,num):
        if (num%i)==0:
        	return False

    return True


def gen_primes(max_number):
	for num1 in range(2, max_number):
		if isprime(num1):
			yield num1


prime= gen_primes(50)
print("prime", next(prime))
print("prime", next(prime))
print("prime", next(prime))
print("prime", next(prime))


# generator expressions

double =(x * 2 for x in range(10))
print("double:", next(double))
print("Double:", next(double))
print("double:", next(double))