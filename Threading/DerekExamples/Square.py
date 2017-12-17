# example demonstrating the usage of getters and setters
class Square:
	def __init__(self, height="0",width="0"):
		self.height=height
		self.width=width

	@property
	def height(self):
		print("Retrieving the Height")
		return self.__height

	@height.setter
	def height(self,value):
		if value.isdigit():
			self.__height=value

		else:
			print("Please only enter numbers for height")


	@property
	def width(self):
		print("Retrieving the width")
		return self.__width

	@width.setter
	def width(self,value):
		if value.isdigit():
			self.__width=value

		else:
			print("Please only enter numbers for width")

	def getArea(self):
		val= int(self.height) * int(self.width)
		return val


def main():
	asquare=Square()

	height= input("enter height")
	width= input("Enter width")
	asquare.height=height
	asquare.width=width
	print("Height",asquare.height)
	print("Width",asquare.width)
	print("The area is ",asquare.getArea())

main()