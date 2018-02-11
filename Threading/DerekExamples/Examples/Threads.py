# Threads.py

import threading
import time
import random

def executeThread(i):
	print("Thread{} sleeps at{}".format(i, time.strftime("%H:%M:%S",time.gmtime())))
	randslepTime= random.randint(1,5)

	time.sleep(randSleepTime)

	print("Threads{} stops sleeping at {} ".ormat(i, time.strftime("%H:%M:%S",time.gmtime())))


	for i in range(10):
		thread= threading.Thread(target=executeThread,args=(i,))

		thread.strat()

		print("Active Threads:", threading.activeCount())

		print("Thread OBjects:", threading .enumerate())
		
