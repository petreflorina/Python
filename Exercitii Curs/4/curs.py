def dice():
	n = 7
	print [(i,j) for i in range (n) for j in range(n)]

dice()

def no_duplicates(my_list):
	no_dupes = []
	[no_dupes.append(i) for i in my_list if not no_dupes.count(i)]
	return no_dupes

list = [1,1,3,5,6,7,3]
print no_duplicates(list)


def dictionaire():
	result = []
	firm = [("Pixar", 2), ("Disney", 4), ("Warner Bros", 9), ("Universal", 5), ("Reception", 0), ("Studio Ghibli", 8), ("DreamWorks", 6)]
	result = {key : firm for (firm, key) in firm}  

	print result


dictionaire()

def zen():
	words_list = []
	with open('this.txt', 'r') as f:
		words_list = [x for x in f.read().split()]
	
	better_index = []
	
	[better_index.append(i) for i, item in enumerate(words_list) if item == 'better']
	print better_index

zen()