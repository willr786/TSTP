def square_num(num):
  """This function squares the number that the user inputs."""
  num = int(num)
  square = num ** 2

  return square

while True:
  try:
    val = input("Please enter a number: ")
    if val == 'q':
      break
    squared_val = square_num(val)
  except ValueError:
    print("You must enter a number value!!!")
  else:
    print("This is your number squared: " + str(squared_val))