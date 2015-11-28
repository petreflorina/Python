def fact(n):
	
	x = 1
	for elem in range(1, n):
		x = x * elem

	x = x * n
	print x

fact(3)