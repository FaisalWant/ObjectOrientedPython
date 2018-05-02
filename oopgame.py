# oop game in python

class Blob:

  def __init__(self, color):
      self.x=random.randrange(0,WIDTH)
      self.y=random.randrange(0,HEIGHT)
      self.size=random.randrang(4,8)

  def move(self):
      self.move_x= random.randrange(-1,2)
      self.move_y=random.randrange(-1,2)
      self.x += self.move_x
      self.y+=self.move_y


      if self.x<0:
         self.x=0

      elif self.x>WIDTH:
         self.x=WIDTH

       if self.y<0:
         se    