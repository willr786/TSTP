class Apple():
	"""This is a class that describes an apple."""
	def __init__(self, col, s, var):
		self.color = col
		self.size = s 
		self.variety = var
		print("Here is an apple")
		
app1 = Apple('red', 'small', 'washington') 
app2 = Apple('green', 'large', 'macintosh')
