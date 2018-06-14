class Horse():
	def __init__(self, name, breed, owner):
		self.name = name
		self.breed = breed
		self.owner = owner
		
class Rider():
	def __init__(self, name):
		self.name = name
	
will = Rider('Will Robinson')	
my_horse = Horse('Claudia', 'Andalusian', will)
print(my_horse.name)
print(my_horse.breed)
print(my_horse.owner.name)

