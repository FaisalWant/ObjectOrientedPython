class IntSet(object):
  """ An intset is a set of integers"""

  # Information about the implementation (not abstraction)
  # The value of the et is represented by a list of ints
  # Each int in thin set occurs in self.vals exactly once

  def __init__(self):
    self.vals=[]

  def insert(self, e):
    """ Assume e is an integer an insert e into self"""
    if not e in self.vals:
        self.vals.append(e)


  def member(self,e):
    """ Assume e is an integer 
        Returns True if e is in self and Fals otherwise"""
    return e in self.vals

  def remove(self,e):
    """ Assume e is an integer and removes e from self raises
    value Error if e is not in self"""

    try:
        self.vals.remove(e)
    except:
        raise ValeError(str(e)+'Not found')

  def getMembers(self):
    """ Returns a list containing the elements of self.
     Nothing can be assumed about the order of the elements"""
    return self.vals[:]
  def __str__(self):
    """Returns a string representation of self"""
    self.vals.sort()
    result=''
    for e in self.vals:
        result= result+str(e)+','
    return '{' + result[:-1] +'}'    




s= IntSet()
s.insert(3)
s.insert(4)
print(s)