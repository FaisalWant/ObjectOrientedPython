
import threading
import time
import random


class BankAccount(threading.Thread):
	acctBalance=100
	def __init__(self,name,moneyRequest):
		threading.Thread.__init__(self)
		self.name= name
		self.moneyRequest=moneyRequest

	def run(self):
		threadLock.acquire()
		BankAccount.getMoney(self)
		threadLock.release()

	@staticmethod
	def getMoney(customer):
		print("{} tries to withdrawl ${} at {}".format(customer.name,  customer.moneyRequest,  time.strftime("%H,%M,%S",time.gmttime())))
		if BankAccount.acctBalance-customer.moneyRequest >0:
		   BankAccount.acctBalance-=customer.moneyRequest
		   print("New account Balance:${}".format(BankAccount.acctBalance))
			
		else:
		   print("Not enought money in account")
		   print("Current balance: ${}".format(BankAccount.acctBalance))

	time.sleep(3)



threadLock= threading.Lock()
doug=BankAccount("Doug",1)
Faisal=BankAccount("Faisal",100)
sally=BankAccount("sally",50)
doug.start()
Faisal.start()
sally.start()

doug.join()
Faisal.join()
sally.join()

print("Execution Ends")   		
