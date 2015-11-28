
def div():
	i = 0
	a = []
	for elem in range(2000, 3000):
		if elem % 7 != 0 and elem % 5 == 0:
			a.append(elem)

	if 3000 % 7 != 0:
		a.append(3000) 
	print a
	
div()