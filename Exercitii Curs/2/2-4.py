
import random

def random_cards():
	number = [2,3,4,5,6,7,8,9,10,'A','J','Q','K']
	_type = ['romb','trefla','inima rosie','inima neagra']

	for i in range(5):
		print random.choice(number), random.choice(_type)
		
random_cards()
