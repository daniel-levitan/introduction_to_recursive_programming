def print_digits(n):
	l = len(str(n)) 
	if l == 1:
		print(n)
	else:
		dig = n // (10 ** (l - 1))
		print(dig)
		print_digits(n - dig * (10 ** (l - 1)))


def main():
	n = 2743
	print_digits(n)


if __name__ == '__main__':
	main()
