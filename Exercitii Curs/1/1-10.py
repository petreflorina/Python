
def intersect(a, b):
	ok = False
	for elem in range(0, len(a)):
		if a[elem] in b:
			ok = True
	print ok

a = [6,7,8,9,11,'ana']
b = [11,2,'ana']
intersect(a,b)