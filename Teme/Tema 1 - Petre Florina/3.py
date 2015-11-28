import json
from datetime import datetime
import re

DATE_FORMAT = '%d.%m.%Y'


def get_age(date_of_birth):
	now = datetime.now()
	return now.year - date_of_birth.year - \
	((date_of_birth.month, date_of_birth.day) > (now.month, now.day))


def get_email(text):
	email_pattern = '^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}S'
	match = re.search(email_pattern, text)
	if match:
		return match.group()

if __name__=='__main__':

	with open('input.json', 'r') as f:
		content = json.load(f)

	birthdays = []
	ages = []
	years = set()
	emails_dict = []
	for person in content:
		birthday = datetime.strptime(person['birthday'], DATE_FORMAT)
		birthdays.append(birthday)
		ages.append(get_age(birthday))
		years.add(birthday.year)
		emails_dict[person['nume']] = get_email(person['about'])
	medium_age = sum(ages) / len(ages)
	
	print medium_age	