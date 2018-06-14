print("I wrote a \" \".  I sent it to \" \"!")
response_1 = input("Please enter a word to fill in the sentence above: ")
response_2 = input("Please enter another for the second portion: ")

print()

filled_in_phrase = "I wrote a {}.  I sent it to {}.".format(response_1,response_2) 
print(filled_in_phrase)
