
import random

def ghiceste():
	random_no = random.randint(1, 20)

 	print 'Ai posibilitatea sa ghicesti numarul la care m-am gandit din 5 incercari. Esti pregatit? Sa ii dam drumul!'
 	ok = 0;

 	for i in range(5):
 		if ok == 0:
	 		x = input('incercarea')
	 		print i

	 		if x == random_no:
	 			print 'Felicitari! Ai reusit din a ', i, '-a incercare'
	 			ok = 1
	 		else:
	 			if nr > x :
	 				print 'Gresit! Numarul meu este mai mare.'
	 			else:
	 				print 'Gresit! Numarul meu este mai mic.'
	 if ok == 0:
	 	print 'Imi pare rau, nu ai reusit sa afli numarul.'

ghiceste()
