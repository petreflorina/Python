
for elem in range(1,100):
	ok = 0;
	if elem % 3 == 0:
		if elem % 5 == 0:
			print 'fizz buzz'
			ok = 1
		else: 
			print 'fizz'
			ok = 2

	if elem % 5 == 0 and ok == 0:
		print 'buzz'
	else:
		if ok != 2:
			print elem
