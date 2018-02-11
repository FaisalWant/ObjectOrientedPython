# iterabAndItera.py
# iterators, iterable, generatingfunctions


# sampStr= iter("Sample")

# print("Char:", next(sampStr))
# print("Char:", next(sampStr))
# print("Char:", next(sampStr))

# creating a custom iterator for  a custom class



# class Alphabet:

# 	def __init__(self):
# 		self.letters= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 		self.index= -1

# 	def __iter__(self):
# 		return self

# 	def __next__(self):
# 		if self.index > = len(self.letters)-1:
# 		   raise StopIteration
# 		self.index +=1
# 		return self.letters[self.index]


# alpha= Alphabet()

# for letter in alpha:   #here lett
#    print(letter)

# Accessing Dictionary using keys
#-------------------------------------
# derek={"fName":"Faisal", "lName":"Afzal"}

# for key in derek:
# 	print(key, derek[key])


# problem 
# create a class that returns values from the Fibonacci
# sequence each time next is called
# FIB:1
# FIB:2
# FIB:3
# FIB:5
class Fibonacci:
	def __init__(self):
		self.first=0
		self.second=1

	def __iter__(self):
		return self

	def __next__(self):
		fibNum= self.first+self.second
		self.first= self.second
		self.second= fibNum
		return fibNum

fibSeq= Fibonacci()
for i in range(10):
	print("FIb", next(fibSeq))


												 


