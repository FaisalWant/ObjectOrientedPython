#Drunk.py

class Drunk(object):
	def __init__(self,name=None):
		""" Assumes name is a str"""
		self.name= name

	def __str__(self):
		if self!=None:
			return self.name

		return 'Anonymous'

class UsualDrunk(Drunk):
	def takeStep(self):
		stepChoices=[(0.0,1.0),(0.0,-1.0),(1.0,0.0),(-1.0,0.0)]
		return random.choice(stepChoices)



def walk(f,d,numSteps):
	""" Assumes: f a Field
	d a Drunk in f and 
	numSteps an int >=0"""
	start = f.getLoc(d)
	for s in range(numSteps):
		f.moveDrunk(d)
	return start.distFrom(f.getLoc(d))

def simWalks(numSteps,numTrials,dClass):
	""" Assumes numsteps an int >=0 numTrials an int >0
	dClass a subclass of drunk
	simulates numTrials wlaks of numsteps steps each

	"""
	Homer= dClass()
	origin= Location(0.0,0.0)
	distances=[]
	for t in range(numTrials):
		f= Field()
		f.addDrunk(Homer,origin)
		distance.append(walk(f,Homer,numTrials))
    return distances

def drunkTest(walkLengths,numTrials,dClass):
	""" Assumes walklegnths as a sequence of ints >=0

	numTirials an int >0 , dClass a subclass of Drunk
	for each number of steps in walkLenghts, run simwlaks with
	numTrials  wlak and pwints results"""
    for numSteps in walkLenghts:
    	distance= simWalks(numSteps,numTrials,dClass)
    	print (dClass.__name__, 'random walk of ', numSteps,'steps'
        print('Mean= ',sum(distances)/len(distances),\
        	'cv=',CV(distances))
        print ('Max=', max(distances), 'Min=',min(distances))