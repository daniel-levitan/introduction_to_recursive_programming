VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def count_vowels(s):
	if len(s) == 0:
		return 0
	else:
		if s[0] in VOWELS:
			return 1 + count_vowels(s[1:])
		else:
			return count_vowels(s[1:])

def main():
	s = 'abc'
	print(s, count_vowels(s))

	s = 'bcd'
	print(s, count_vowels(s))

	s = 'aAEeIi'
	print(s, count_vowels(s))




if __name__ == '__main__':
	main()