#MITPerson.py
from Person import Person
class MITPerson(Person):
	nextIdNum= 0  # identification number

	def __init__(self,name):
		Person.__init__(self,name)
		self.idNum=MITPerson.nextIdNum
		MITPerson.nextIdNum+=1
	def getIdNum(self):
		return self.idNum

	def __lt__(self,other):
		return self.idNum<other.idNum

	def isStudent(self):
		return isinstance(self,Student)


if __name__ == "__main__":
	p1= MITPerson('Faisal Wanth')
	print (str(p1)+ '\'s id number is '+ str(p1.getIdNum()))