import cubed

val = input("Enter a number to be cubed: ")
val = int(val)
val_cubed = cubed.cube_value(val)

print("This is your number cubed: " + str(val_cubed))