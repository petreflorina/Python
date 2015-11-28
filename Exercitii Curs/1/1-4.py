

a = [1, 3, 20, 1024, 53, 12, 102, 1, 4, 43, 32]
b = []
indexB = 0

for elem in range (len(a)):
	if elem % 2 == 1:
		b[indexB] = a[elem]
		index += 1
print b