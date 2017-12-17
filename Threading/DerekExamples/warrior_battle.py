import math
import random

class Warrior:
	def __init__(self,name="Warrior",health=0,attkMax=0,blockMax=0):
		self.name= name
		self.health=health
		self.attkMax=attkMax
		self.blockMax=blockMax

	def attack(self):
		attkAmt=self.attkMax*(random.random()+.5)
		return attkAmt


	def block(self):
		blockAmt= self.blockMax*(random.random()+.5)
		return blockAmt

class Battle:
	def startFight(self, warrior1,warrior2):
		while True:
		   if self.getAttackResult(warrior1,warrior2)=="GameOver":
			   print("GameOver")
			   break

		   if self.getAttackResult(warrior2,warrior1)=="GameOver":
			   print ("Gameover")
			   break
	@staticmethod
	

	def getAttackResult(warriorA,warriorB):
		warriorAAttkAmt= warriorA.attack()
		warriorBBlockAmt= warriorB.block()
		damage2WarriorB= math.ceil(warriorAAttkAmt-warriorBBlockAmt)
		warriorB.health= warriorB.health-damage2WarriorB
		print("{} attack {} and deals {} damage".format(warriorA.name,
			warriorB.name,damage2WarriorB))
		print("{} is down to {} health".format(warriorB.name,warriorB.health))
		
		if warriorB.health <= 0:
			 print("{} has Died and {} is Victorious".format(warriorB.name,warriorA.name))
			 return "GameOver"

		else:
			return "Fight Again"


def main():
	maximus= Warrior("Maximus",50,20,10)
	galaxon= Warrior("Galaxon",50,20,10)

	battle= Battle()
	battle.startFight(maximus,galaxon)
main()