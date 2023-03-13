def summ(n):
	if n == 1:
		return 1
	elif n % 2 == 1:
		return 2 * summ((n - 1) // 2) + ((n + 1) // 2) ** 2
	else:
		return 2 * summ(n // 2) + (n // 2) ** 2


def main():
	n = 6 # 21
	print(n, summ(n))

	n = 5 # 15
	print(n, summ(n))


if __name__ == '__main__':
	main()