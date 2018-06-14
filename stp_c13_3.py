class Shape():
	#def __init__(self):
		
	def shape_id(self):
		print("I am a shape!")

class Square(Shape):
	def __init__(self, s1):
		self.s1 = s1
	
	def calculate_perimiter(self):
		self.perimeter = self.s1 * 4
		print("The permiter of this square is: " + str(self.perimeter))
	
		
class Rectangle(Shape):
	def __init__(self, length, width):
		self.length = length
		self.width = width
	
	def calculate_perimiter(self):
		perimeter = (2 * self.length) + (2 * self.width)
		print("The permiter of this rectangle is: " + str(perimeter))
		
		
my_shape = Shape()
my_shape.shape_id()

print()

my_square = Square(5)
my_square.shape_id()
my_square.calculate_perimiter()

print()

my_rectangle = Rectangle(3,6)
my_rectangle.shape_id()
my_rectangle.calculate_perimiter()
