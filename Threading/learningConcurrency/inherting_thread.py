#inherting_thread.py

from threading import Thread 
class myWorkerThread(Thread):
	def __init__(self):
		print("Hello World")
		Thread.__init__(self)
	def run(self):
		print("Thread is now running")




myThread= myWorkerThread()
print("created my Thread Object")
myThread.start()

print("Started my thread")

myThread.join()

print("My Thread finished")
