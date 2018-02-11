#inheritance,polymorphism and magicmethods


class Animal:
	def __init__ (self, birthType= "UNKNOWN", appearance="UNKNOWN",blooded= "UNKNOWN"):
	   self.birthType= birthType
	   self.appearance= appearance
	   self.blooded= blooded


	@property 
	def birthType(self):
		return self.__birthType

	@birthType.setter
	def birthType(self, birthType):
		self.__birthType= birthType

	@property 
	def appearance(self):
		return self.__appearance

	@appearance.setter
	def appearance(self, appearance):
		self.__appearance= appearance
		
	@property 
	def blooded(self):
		return self.__blooded

	@blooded.setter
	def blooded(self, blooded):
		self.__blooded= blooded
		

	def __str__(self):
		return "A{} is {} it is {} it is {} ". format(type(self).__name__,self.birthType,self.appearance, self.blooded)



class Mammal(Animal):
	def __init__(self, birthType= "born alive", appearance= "hair or fur", blooded= "warm blooded", nurseYoung=True):
	   Animal.__init__(self, birthType, appearance, blooded)
	   self.__nurseYoung= nurseYoung


	@property 
	def nurseYoung(self):
		return self.__nurseYoung

	@nurseYoung.setter
	def nurseYoung(self, nurseYoung):
		self.__nurseYoung= nurseYoung
	
	def __str__(self):
		return super().__str__() +"and it is {} they nurse their young".format(self.nurseYoung)


class Reptile(Animal):
	def __init__(self, birthType= "born in an egg or born alive", appearance= "hair or fur", blooded= "cold blooded"):
		Animal.__init__(self, birthType, appearance, blooded)

	def sumAll(self,*args):
		for i in args:
			sum+=i
		return sum

class Time:
	def __init__(self, hour=0, minute=0, second=0):
		self.hour= hour
		self.minute= minute
		self.second= second

	def __str__(self):
		return "{}:{:02d}:{:02d}".format(self.hour,self.minute, self.second)

	def __add__(self, other_time):
		new_time= Time()
		
		# Add the seconds and correct if sum>60
		if(self.second+other_time.second)> 60:
			self.minute+=1

			new_time.second= (self.second+other_time.second)-60
		else:
			new_time.second= self.second-other_time.second


		# add the minutes and correct if sum is >60
		new_time= Time()
		
		# Add the seconds and correct if sum>60
		if(self.minute+other_time.minute)> 60:
			self.minute+=1

			new_time.minute= (self.minute+other_time.minute)-60
		else:
			new_time.minute= self.second-other_time.minute




		# add the hours and correct fi sum > 24

		new_time= Time()
		
		# Add the seconds and correct if sum>60
		if(self.hour+other_time.hour)> 24:
			self.hour+=1

			new_time.hour= (self.second+other_time.hour)-24
		else:
			new_time.hour= self.second-other_time.hour
		 

		return new_time




def main():
	# animal1= Animal("born alive")
	# print(animal1.birthType)
	# print(animal1)


	# mammal1= Mammal()
	# print(mammal1.birthType)
	# print(mammal1.appearance)
	# print(mammal1.blooded)
	# print(mammal1.nurseYoung)
	# print(mammal1)


	# reptile1= Reptile()
	# print(reptile1.birthType)
	# print(reptile1)


	#print("Sum:{}".format(reptile1.sumAll(1,2,3,4,5)))
	

	time1= Time(1,20,30)

	print(time1)

	time2= Time(24,41,30)

	print(time1 +time2)


main()