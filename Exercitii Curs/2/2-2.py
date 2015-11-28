import random

def random_lines():
	with open('impar.txt', 'w') as f:
		for i in range(random.randrange(1,10,2)):
			f.write(random.randrange(100,1000,2))

random_lines()
