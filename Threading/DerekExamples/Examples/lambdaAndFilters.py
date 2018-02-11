# lambdaAndFilters.py


# def get_func_mult_by_num(num):

#    def mult_by(value)

#        return num* value

#    return mult_by

# generated_func= get_func_mult_by_num(5)

# print("5*10", generated_func(10))



# listOfFuncs= [times_two, generated_func]

# print("5*9", listOfFuncs[1](9))



# #############################
# # Create a function that receives a list and a function 
# # The function passed will return True or False if a list value is odd
# # The surrounding function will return a list of odd numbers

# myList=[1,3,5,7,9]

# def is_it_odd(num):
# 	if num%2==0:
# 		return False
# 	else:
# 		return True




# def give_me_list(list, func):
# 	oddList=[]

# 	for i in list:
# 		if func(i):
# 			oddList.append(i)

# 	return oddList

# aList= range(1,20)

# print(give_me_list(aList,is_it_odd))


#*************************************
#functional annotation   (used for documentations)
#-3----------------------
# def random_func(name:str, age:int, weight:float)->str:
#      print("Name", name)
#      print("Age", age)
#      print("weight", weight)


#      return "{} is {} yeas old and weights{}".format(name, age, weight)

# print(random_func("faisal", 41, 181))

# sum = lambda x,y: x+y
# print("Sum:", sum(4,5))


# #--------------------------
# can_vote= lambda age:True if age>=18 else False

# print("can vote :", can_vote(19))

# #---------------------------
# #lambda in lists
# powerList=[lambda x:x**2, 
#             lambda x:x**3, 
#             lambda x:x**4]

# for func in powerList:
# 	print(func(4))


#lambda in dictionaries


# attack ={'quick': (lambda : print("QuickAttack"))
#           'power': (lambda : print("powerAttack"))
#           'miss': (lambda : print("MissedAttack"))

#         }

# attack['quick']()

# import random
# attackkey= random.choice(list(attack.keys()))  
# attack[attackkey]()        

# problemm
#-----------
# create a random list filled with the characters H and True
# for heads and tails. Output the number of Hs and tail
# Example Output
# Heads:46
# Tails:54
# import random
# #create the list
# flipList=[]

# #populate the list with 100 Hs Tails
# for i in range(1, 10):
#     flipList+=random.choice(['H','T'])

# #output the results

# print("Heads:", flipList.count('H'))
# print("Tails", flipList.count('T'))

# oneTo10= range(1,11)
# def dbl_num(num):
#     return num*2

# print(list(map(dbl_num,oneTo10)))

# alist= list(map((lambda x,y:x+y), [1,2,3],[5,6,1]))
# print(alist

# problem
# ----------------
# Find the multiples of 9 from a random 100 value list with values
# between 1 and 1000
import random

#one method

myList=list()
for i in range(1000):
   myList.append(random.randint(1,1000))


# creating list using list comprehension

newList=[random.randint(1,1001) for i in range(1000)]

# print(myList)

# print("\n")

# print(newList)
# hylist=[i for i in newList if i%9==0]
# print(hylist)



# reduce

from functools import reduce
print(reduce((lambda x,y :x+y), range(1,6)))