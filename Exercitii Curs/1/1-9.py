
def is_palindrom(word):
	second_word = ""
	for elem in reversed(word):
		second_word += elem

	if word == second_word:
		print True
	else:
		print False

is_palindrom('mama')