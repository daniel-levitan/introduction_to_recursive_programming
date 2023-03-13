# We will represent Mary win as the string "Mary" and 
# John win as the string "John"
def play_Mary(n):
	if n == 1 or n == 3 or n == 4:
		# print('Mary wins')
		return "Mary"
	elif n == 2:
		# return "John"
		return play_John(n - 1)
	else: # n > 4
		return play_John(n - 4)


def play_John (n):
	if n == 1 or n == 3 or n == 4:
		# print('John wins')
		return "John"
	elif n == 2:
		# return "Mary"
		return play_Mary(n - 1)
	else:
		# John removes one pebble
		return play_Mary(n - 1) # Turn switches to Mary


def main():
	result = {'Mary': 0, 'John': 0}
	Mary_started = {'Mary': 0, 'John': 0}
	John_started = {'Mary': 0, 'John': 0}

	# print("First move is from John")
	for n in range(1, 101):
		result[play_John(n)] += 1
		John_started[play_John(n)] += 1
		# print(play_John(n))

	# print()
	# print("First move is from Mary")
	for n in range(1, 101):
		result[play_Mary(n)] += 1
		Mary_started[play_Mary(n)] += 1

	print("Total number of victories")
	for key, val in result.items():
		print(key, val)

	print()
	print("First move is from John")
	for key, val in John_started.items():
		print(key, val)

	print()
	print("First move is from Mary")
	for key, val in Mary_started.items():
		print(key, val)

	print()


if __name__ == '__main__':
	main()