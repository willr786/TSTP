def name(first_name, middle_name='', last_name=''):
  """This function allows the user to enter his/her name."""
  full_name = first_name + ' ' + middle_name + ' ' + last_name
  return full_name

f_name = input("Please enter your name fist name: ")
m_name = input("Please enter your middle name if you have one: ")
l_name = input("Please enter your last name if you want to: ")
output = name(f_name, m_name, l_name)

print("Hello, " + output + "!")