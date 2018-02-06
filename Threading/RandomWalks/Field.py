#Field.py


class Field(Object):
	def __init__(self):
		self.drunks={}

	def addDrunk(self,drunk,loc)
	   if drunk in self.drunks:
	   	  raise ValueError("Duplicate drunk")

	   else:
	   	  self.drunks[drunk]=loc
	def moveDrunk(self,drunk):
		if drunk not in self.drunks:
			raise ValueError('Drunk not in field')

		xDist,yDist= drunk.takeStep()
		currentLocation= self.drunks[drunk]
		# use move method of location to get new location
		self.drunks[drunk]= currentLocation.move(xDist,yDist)


	def getLoc(self,drunk):
		if drunk not in self.drunks:
			raise ValueError('Drunk not in field')

		return self.drunks[drunk]