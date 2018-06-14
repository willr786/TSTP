tv_shows = ['The Walking Dead',
			'Entourage',
			'The Sopranos',
			'The Vampire Diaries']
			
for show in tv_shows:
	print(show)

for i in range(0,5):
	print(i)


print()	

# The book solution
for index, show in enumerate(tv_shows):
	print(index)
	print(show)
