#staticClass.py

class Dog:
	num_of_dogs=0 
	def __init__(self,name="Unknow"):
		self.name=name
		Dog.num_of_dogs+=1

	@staticmethod
	def  getNumOfDogs():
		print("There are currently {} dogs".format(Dog.num_of_dogs))

def main():
	spot= Dog("Spot")
	doug=Dog("doug")
	spot.getNumOfDogs()
	doug.getNumOfDogs()
main()
