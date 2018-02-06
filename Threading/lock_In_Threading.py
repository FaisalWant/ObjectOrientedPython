#example:3 lock_In_Threading.py

import threading

# global variable x
x=0

def increment():
	""" function to incremnt global variable x"""
	global x
	x+=1
def thread_task(lock):
	""" task for thread 

	    class increment fucntion 100000 times."""
	for _ in range(100000):
		lock.acquire()
		increment()
		lock.release()


def main_task():
	global x
	# setting global variab x as 0
	x=0
	# creating a lock 

	lock= threading.Lock()
	# creating threads
    # lock in passed as target function argument
	t1= threading.Thread(target= thread_task,args=(lock,))
	t2= threading.Thread(target=thread_task,args=(lock,))

	t1.start()
	t2.start()
	# wait until threads finish their job

	t1.join()
	t2.join()
if __name__=="__main__":
	for i in range(10):
		main_task()
		print("Iterataion{0}:x={1}".format(i,x))
