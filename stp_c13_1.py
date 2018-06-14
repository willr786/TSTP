class Rectangle():
	def __init__(self, length, width):
		self.length = length
		self.width = width
	
	def calculate_perimiter(self):
		perimeter = (2 * self.length) + (2 * self.width)
		print("The permiter of this rectangle is: " + str(perimeter))
		
class Square():
	def __init__(self, s1):
		self.s1 = s1
	
	def calculate_perimiter(self):
		self.perimeter = self.s1 * 4
		print("The permiter of this square is: " + str(self.perimeter))		
		
my_rectangle = Rectangle(3, 6)
my_rectangle.calculate_perimiter()

my_square = Square(4)
my_square.calculate_perimiter()
