
def find_longest_word(a):
	max_length = 0
	for elem in a:
		if len(elem) > max_length:
			max_length = len(elem)
	return max_length

a = ['ana','casa','parapet','masina']
print find_longest_word(a)