
def decode(a):
	b = ''
	for elem in a:
		if elem != ' ':
			b += (chr(ord(elem)+1))
		else:
			b += ' '
	print b
a = "j mjlf cjh cvuut boe j dboopu mjf\nzpv puifs cspuifst dbo'u efoz"
decode(a)
