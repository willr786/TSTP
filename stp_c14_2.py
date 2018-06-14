class Square():
	
	square_list = []
	
	def __init__(self, s1):
		self.s1 = s1
		self.square_list.append(self.s1)
		print("""{} by {} by {} by {}""".format(self.s1, self.s1, 
													self.s1, self.s1))
	
	def calculate_perimiter(self):
		self.perimeter = self.s1 * 4
		print("The permiter of this square is: " + str(self.perimeter))	

sq1 = Square(10)
sq2 = Square(15)
sq3 = Square(30)
sq4 = Square(50)

