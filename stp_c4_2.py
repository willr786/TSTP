def phrase(word):
  """A function that allows a user to enter some type of word or words."""
  your_word = "This is what you entered: " + word  

  return your_word

while True:
  
  entry = input("Please enter a word or some words: ")
  output = phrase(entry)

  if entry == 'q':
    break
  else:
    continue  

  print(output)
