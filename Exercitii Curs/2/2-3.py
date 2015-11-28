
from datetime import date

def birth_days():
	days = 0
	with open('birth.txt', 'r') as f:
		days = (int(date.today().year) - int(f.read(4))) * 365
	bisect_years = 5
	
	print days + bisect_years, 'days'

birth_days()