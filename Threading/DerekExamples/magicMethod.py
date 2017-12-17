#magicMethod.py

class Time:
	def __init__(self,hour=0, minute=0,second=0):
		self.hour= hour
		self.minute=minute
		self.second=second


	def __str__(self):
		 return "{}:{:02d}:{:02d}".format(self.hour,self.minute,self.second)
	
	def __add__(self,other_time):
		 new_time=Time()

		# Add the seconds and corrent if sum>60
		 if(self.second+other_time.second)>=60:
			self.minute+=1
			new_time.second=(self.second+other_time.second)-60
		 else:
			new_time.second=self.second-other_time.second
		

		# add the minute and correct if sum is >60
		 if(self.minute+other_time.minute)>=60:
			self.minute+=1
			new_time.minute=(self.minute+other_time.minute)-60
		 else:
			new_time.minute=self.second-other_time.minute

		# add the hours and correct if sum is >24
		 if(self.hour+other_time)>24:
			new_time.hour=(self.hour+other_time.hour)-24
		 else:
			new_time.hour=self.hour+other_time.hour

		 return new_time

def main():
	time1= Time(1,20,30)
	print(time1)
main()


