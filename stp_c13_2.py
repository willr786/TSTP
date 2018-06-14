class Square():
	def __init__(self, s1):
		self.s1 = s1
		
	def square_size(self):
		print("This square has four sides that equal: " + str(self.s1))
		
	def change_size(self,cval):
		new_size = cval + self.s1
		print("The new size of each side is: " + str(new_size)) 
		
my_square = Square(8)
my_square.square_size()
my_square.change_size(-4)

