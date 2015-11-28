
def test_numar(s):
	import re

	phone = re.compile(r'021([0-9]{7})')
	if (phone.search(s)):
		print True
	else:
		print False

test_numar('numarul meu este 0210123456, sa stii')
