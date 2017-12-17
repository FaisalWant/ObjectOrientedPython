#Student.py

from MITPerson import MITPerson
class Student(MITPerson):
	pass

class UG(Student):
	def __init__(self,name,classYear):
		MITPerson.__init__(self,name)
		self.year=classYear

	def getClass(self):
		return self.year

class Grad(Student):
	pass

if __name__=="__main__":
	p5= Grad('Buzz Aldrin')
	p6= UG('Billy Beaver',1984)
	print(p5,'is a graduate student is',type(p5)==Grad)
	print(p5,'is an undergraduate student is',type(p5)==UG)