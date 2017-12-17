# examp 1:cubeThreading.py

# ptython proram to illustrate the concept 
# of threading 
# importing the threading module

import threading

def print_cube(num):
   """ function to print cube of given num"""
   print("Cube:{}".format(num*num*num))

def print_square(num):
	""" function to print square of give num"""
	print("square:{}".format(num*num))

if __name__ == "__main__":
	# creating thread
	t1= threading.Thread(target=print_square,args=(10,))
	t2= threading.Thread(target=print_cube,args=(10,))
   
	t1.start()
	t2.start()

	# wait until  thread 1 is completely executed

	t1.join()
	# wait until thread 2 is completely executed
	t2.join()

	# both threads completely executed

	print("Done!")