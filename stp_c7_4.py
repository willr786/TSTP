nums = [2, 4, 6, 8, 10]

while True:
	guess = input("Enter a number or 'q' to quit: ")
	
	if guess == 'q':
		break
	
	try:
		guess = int(guess)
	except ValueError:
		print("Please enter a number or 'q'!!!")	
	
	if guess in nums:
		print("That's one of my numbers!!!")
	else:
		print("Try another number.")
