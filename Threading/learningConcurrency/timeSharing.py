#timeSharing.py
import threading
import time
import random
counter=1
def WorkerA():
	global counter
	while counter<1000:
		counter+=1
		print("Worker A is  incrementing counter to {}".format(counter))
		sleepTime=random.randint(0,1)
		time.sleep(sleepTime)
def WorkerB():
	global counter
	while counter >-1000:
		counter-=1
		print("worker B is decrementing counter to {}".format(counter))
		sleepTime= random.randint(0,1)
		time.sleep(sleepTime)

def main():
	t0= time.time()
	thread1= threading.Thread(target=WorkerA)
	thread2=threading.Thread(target=WorkerB)
	thread1.start()
	thread2.start()
	thread1.join()
	thread2.join()
	t1=time.time()
	print("Execution Time{}".format(t1-t0))



if __name__== '__main__':
	main()