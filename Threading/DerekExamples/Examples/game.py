# #game.py
# sam attacks paul and deals 9 damage
# paul is down to 10 health
# paul attacks sam and deals 7 damage
# sam is down to 7 health
# sam attacks paual and deals 19 damage
# paul is down to -9 health 
# paut had died and sam is victorious
# GAME OVER


import random
import math
# warrior & Battle class
class Warrior:
	def __init__(self, name= "Warrior",health=0, attkMax=0, blockMax=0):
		self.name= name
		self.health= health
		self.attkMax= attkMax
		self.blockMax= blockMax

	def attack(self):
		attkAmt= self.attkMax *(random.random()+.5)
		return attkAmt

	def block(self):
		blockAmt= self.blockMax *(random.random()+.5)
		return blockAmt

class Battle:
	def startFight(self, warrior1,warrior2):
		while True:
			if self.getAttackResult(warrior1,warrior2)=="GAME OVER":
			   print("GAMEOVER")
			   break
			if self.getAttackResult(warrior2,warrior1)=="GAME OVER":
			   print("GAMEOVER")
			   break
	@staticmethod
	def getAttackResult(warriorA, warriorB):
	   warriorAAttkAmt= warriorA.attack()
	   warriorBBlockAmt= warriorB.block()
	   damage2WarriorB= math.ceil(warriorAAttkAmt-warriorBBlockAmt)
	   warriorB.health= warriorB.health-damage2WarriorB
	   print("{} attacks and deals{}". format(warriorA.name,warriorB.name,damage2WarriorB))

	   print("{} is down to {} health ".format(warriorB.name, warriorB.health))
	   
	   if warriorB.health<=0:
		   print("{} has Died and {} is victorious ".format(warriorB.name, warriorA.name))
		   return "GAME OVER"
	   else :
		   return "FIGHT AGAIN"

def main():
	maximus= Warrior("Maximus",50,20,10)
	galaxon=Warrior ("Galaxon", 50,20,10)
	battle = Battle()

	battle.startFight(maximus,galaxon)

main()






# warriors will have names, health, and attack and block maximums

# They will have the capabilities to attack and block random amounts

# Attack ranmdom()  0.0 to 1.0  * maxAttack +.5

# Block will use random()

#Battle class capability of looping until 1 warrior dies

#warriors will each get a turn to attack each other

#Function gets 2 warriors 

# 1 warrior attacks the other

#Attacks and block be integers
