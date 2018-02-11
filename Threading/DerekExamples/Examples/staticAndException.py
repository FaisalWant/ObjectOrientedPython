#staticAndException

class Sum:
   @staticmethod
   def getSum(*args):
	  sum=0
	  for i in args:
		sum+=i
	  return sum


class Dog:
	num_of_dogs=0          # static field

	def __init__(self, name="UNKNOW"):
		self.name= name

		Dog.num_of_dogs+=1

	@staticmethod
	def getNumOfDogs():
		print("There are curretnly {} dogs".format(Dog.num_of_dogs))



# Exception  raising

class DogNameError(Exception):
	def __init__(self):
		Exception.__init(self, *args, **kwargs)

try : 
	dogName= input("What is your dogs name")

	if any(char.isdigit() for char in dogName):
       raise DogNameError


except DogNameError:
	print("Your dogs name can't containg a number")










def main():
	print("Sum:", Sum.getSum(1,2,3,4))
	spot= Dog("Spot")

	doug=Dog("Doug")

	spot.getNumOfDogs()
	doug.getNumOfDogs()
	Dog.getNumOfDogs()
	print("The number of dogs without using object",Dog.num_of_dogs)
    
    try:
    	aList=[1,2,3]
    	print(aList[3])
    

    except IndexError:
    	print("Sorry that index doesn't exist")

    except:
    	print("An unknown error occured")






main()

