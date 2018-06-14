user_input = input("Enter a word, some words, or a sentence: ")

with open('something.txt', 'w') as f:
	f.write(user_input)
