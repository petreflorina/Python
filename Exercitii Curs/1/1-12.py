

def filter_long_words(a, n):
	b = []
	for elem in a:
		if len(elem) > n:
			b.append(elem)

	return b

n = 3
a = ['ana','casa','parapet','masina']
print filter_long_words(a, n)