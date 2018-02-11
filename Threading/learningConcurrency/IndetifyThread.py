#IndetifyThread.py
# also something like grouping threads

import threading
import time
def myThread():
	print("Thread{} starting".fomat(threading.currentThread().getName()))
	time.sleep(10)
	print("Thread{} ending".format(threading.currentThread().getName()))
	for i in range(4):
		threadName="Thread-" +str(i)
		thread= threading.Thread(name=threadName,targt)

