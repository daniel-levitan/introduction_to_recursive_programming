# Define and code Boolean linear and tail-recursive functions 
# that determine whether a nonnegative integer n contains an odd
# digit.

def contains_odd(n):
	if n < 10:
		return n % 2 == 1
	else:
		if n % 2 == 1:
			return True
		else:
			return contains_odd(n // 10)


def main():
	# n = 1 
	# print(n, contains_odd(n))
	# n = 2 
	# print(n, contains_odd(n))

	n = 246
	print(n, contains_odd(n))
	
	n = 2580
	print(n, contains_odd(n))


if __name__ == '__main__':
	main()