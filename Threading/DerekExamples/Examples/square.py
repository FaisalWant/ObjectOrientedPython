class Square:
	def __init__ (self, height="0", width="0"):
		self.height= height
		self.width= width

	@property            # this is getter 

	def height(self):
		print("Retrieving the Height")

		return self.__height

	@height.setter         # this is setter

	def height(self ,value):
		if value.isdigit():
			self.__height=value

		else: 
		   print("Please only enter numbers for height")

	@property            # this is getter 

	def width(self):
		print("Retrieving the width")

		return self.__width

	@width.setter         # this is setter

	def width(self ,value):
		if value.isdigit():
			self.__width=value

		else: 
		   print("Please only enter numbers for height")

	def getArea(self):
		return int(self.__width)*int(self.__height)

def main():
	asquare= Square()

	height= input("Enter Height")
	width= input("Enter WIdth")
	asquare.height= height
	asquare.width=width

	print("Height", asquare.height)
	print("Width", asquare.width)
	print("The area is ",asquare.getArea())


main() 