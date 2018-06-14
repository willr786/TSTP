class Triangle():
	"""This class represents a triangle."""
	def __init__(self, base, height):
		self.base = base
		self.height = height
		
	def findArea(self):
		return (self.height * self.base)/2
		

my_triangle = Triangle(2, 2)
print(my_triangle.findArea())
