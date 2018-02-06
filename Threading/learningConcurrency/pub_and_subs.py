# pub_and_subs.py
# publisher and subscriber
""" At the poin tof the condition being notifiel, the battle starts
between the two consumers both try to acquire this condition first.
When one wins this fight it then goes on to simply pop this number from
the array"""





import threading
import random
import time
class Publisher (threading.Thread):
	def __init__(self, integers, condition):
		self.condition=condition
		self.integers=integers
		threading.Thread.__init__(self)
	def run(self):
	   while  True:
		  integer= random.randint(0,1000)
		  self.condition.acquire()
		  print("condition Acquired by publisher\
		   {}".format(self.name))
		  self.integers.append(integer)
		  self.condition.notify()   #will notify the object for the new cooked intger
		  print("Condition Released by Publisher:{}".format(self.name))
		  self.condition.release()
		  time.sleep(1)

class Subscriber(threading.Thread):
	def __init__(self, integers, condition):
		self.integers= integers
		self.condition=condition
		threading.Thread.__init__(self)
	def run(self):
		while True:
			self.condition.acquire()
			print("Condition Acquired by consumer \
				:{}".format(self.name))
			while True:
				if self.integers:
					integer= self.integers.pop()
					print("{} Popped from list by consumer:{}".format(integer,self.name))
					break
				print("Condition wait by {}".format(self.name))
				self.condition.wait()


			print("Consumer {} Releasing Condition ".format(self.name))
			self.condition.release()



def main():
	integers=[]
	condition= threading.Condition()
	# Our Publisher

	pub1= Publisher(integers,condition)
	pub1.start()

	#Our Subscriber

	sub1= Subscriber(integers,condition)
	sub2= Subscriber(integers,condition)
	sub1.start()
	sub2.start()
   # Joiing our threads

	pub1.join()

	sub1.join()
	sub2.join()
if __name__=="__main__":
	 main()


