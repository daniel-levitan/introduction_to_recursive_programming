def number_of_ones(n):
	if n < 2:
		return n
	else:
		return n % 10 + number_of_ones(n // 10)


def main():
	n = 11001
	print(number_of_ones(n))


if __name__ == '__main__':
	main()

