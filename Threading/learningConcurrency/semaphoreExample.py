#semaphoreExample.py
"""Semaphores manage a counter representing the number of release() calls minus the number of
acquire() calls, plus an initial value. The acquire() method blocks if necessary until it can return
without making the counter negative. If not given, value defaults to 1"""
class TicketSeller(threading.Thread):
	ticketsSold=0
	def __init__(self, semaphore):
		threading.Thread.__init__(self)  #initialisez the thread
		self.sem=semaphore
		print("Ticker seller Started Work")
	def run(self):
		global ticketAvailable
		running= True
		while running:
			self.randomDelay()
			self.sem.acquire()
			if(tickersAvailable <=0 				
				running=False

			else:
				self.ticketsSold=self.ticketsSold+1
				ticketsAvailabe=ticketsAvailable-1
				print("{} Sold one ({} left)".format(self.getName(),ticketsAvailable))
		    self.sem.release()

		print("Ticket Seller {} sold {} tickets in total".format(self.getName(),self.ticketsSold))
    

    def randomDelay(self):
    	time.sleep(random.randint(0,1))


semaphore= threading.Semaphore()
#our ticket allocation
ticketsAvailable=10
#our array of sellers
sellers=[]
for i in range(4):
	seller= TicketSeller(semaphore)
	seller.start()
	sellers.append(seller)
for seller in sellers
    seller.join()

