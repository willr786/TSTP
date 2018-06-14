def half_num(num):
  """This function divides a number by two."""
  num = int(num)
  half = num/2
  return half

def four_times(num):
  """This function multiplies a number times 4."""
  num = int(num)
  four_x = num * 4
  return four_x

while True:
  try:
    val = input("Please enter a numerical value: ")
    if val == 'q':
      break
    
    result = half_num(val)
    result_2 = four_times(result)
  except ValueError:
    print("You must enter a numerical value!!!")
  else: 
    print(result)
    print(result_2)