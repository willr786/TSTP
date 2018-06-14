from math import pi

class Circle():
	"""This class represents a circle."""
	def __init__(self, radius):
		self.radius = radius
		
	def findArea(self):
		return pi * (self.radius ** 2)
		

my_circle = Circle(8)

print(my_circle.findArea())
