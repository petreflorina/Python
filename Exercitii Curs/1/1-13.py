
def function(*args):
	sum = 0
	for arg in args:
		sum += arg
	return sum

print function(1, 2, 3)