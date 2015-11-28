
def lines():
	nr = 0
	
	with open('input.txt', 'r') as f:
		for line in f:
			nr += 1

	with open('output.txt', 'w') as g:
		g.write(str(nr))

lines()