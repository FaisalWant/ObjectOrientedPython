from Student import Student
from Student import UG
from Student import Grad
class Grades(object):
	""" A mapping from students to a list grades"""
	def __init__(self):
		"""create empyt grade book"""
		self.students=[]
		self.grades={}
		self.isSorted=True

	def addStudent(self,student):
		""" Assumes : student is of type Student 
			ADD studetnt to the grade book"""
		if student in self.students:
			raise ValueError('Duplicate Student')
		self.students.append(student)
		self.grades[student.getIdNum()]=[]
		self.isSorted=False


	def addGrade(self,student,grade):
		""" Assume: grade  is a float
			Add grade to the list of grades for student"""

		try:
			self.grades[student.getIdNum()].append(grade)
		except:
			raise ValueError('Student not in mapping')

	def getGrades(self,student):
		"""Return a list of grades for student"""
		try:# return copy of student's grade
			return self.grades[student.getIdNum()][:]
		except:
			raise ValueError('Student not in mapping')


	def getStudents(self):
		""" Return a list of the students in the grade book"""
		if not self.isSorted:
		   self.students.sort()
		   self.isSorted=True

		for s in self.students:
			yield s
		#return self.students[:]

	def gradeReport(course):
		"""Assumet course if of type Grades"""
		report=''
		for s in course.getStudents():
			tot=0.0
			numGrades=0
			for g in course.getGrades(s):
				tot+=g
				numGrades+=1

			try:
				average=tot/numGrades
				report= report+ '\n '\
				 + str(s) + '\'s mean grade is' +str(average)
			except ZeroDivisionError:
				report =report + '\n' \
						+str(s)+ 'has no grades'

		return report

if __name__== '__main__':
	# ug1=UG('Faisal',2017)
	# ug2=UG('Shumal',2016)
	# ug3=UG('Henry',2015)
	# g1=Grad('Billy Bucker')
	# g2= Grad('Roy Hamot')
	# sixHundred= Grades()
	# sixHundred.addStudent(ug1)
	# sixHundred.addStudent(ug2)
	# sixHundred.addStudent(g1)
	# sixHundred.addStudent(g2)
	# for s in sixHundred.getStudents():
	# 	sixHundred.addGrade(s,75)
	# sixHundred.addGrade(g1,25)
	# sixHundred.addGrade(g2,100)
	# sixHundred.addStudent(ug3)
	# print (Grades.gradeReport(sixHundred))		
	book =Grades()
	book.addStudent(Grad('Faisal'))
	book.addStudent(Grad('Shumal'))
	for s in book.getStudents():
		print s