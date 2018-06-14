def compare(obj1, obj2):
	return obj1 is obj2
	
print(compare('a', 'b'))
print(compare(2, 2))
print(compare(10, 10.0))
