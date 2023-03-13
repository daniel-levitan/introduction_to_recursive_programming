def summ(n):
	if n == 0:
		return 0
	else:
		return summ(n - 1) + n


def main():
	n = 5
	print(summ(n))

	n = 1
	print(summ(n))

	n = 0
	print(summ(n))


if __name__ == '__main__':
	main()