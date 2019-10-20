def is_palindrome(word):
	word2 = ''.join(reversed(word))
	if word == word2:
		return True
	else:
		return False

print(is_palindrome('Deleveled'))
