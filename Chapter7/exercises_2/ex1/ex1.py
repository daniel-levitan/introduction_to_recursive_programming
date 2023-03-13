def binomial(n, m):
	if m == 0 or n == m:
		return 1
	else:
		return binomial(n - 1, m - 1) + binomial(n - 1, m)


def main():
	print(1, binomial(0, 0))
	print(1, binomial(1, 0))
	print(1, binomial(1, 1))
	print(2, binomial(2, 1))
	print(3, binomial(3, 1))
	print(4, binomial(4, 1))
	print(6, binomial(4, 2))



if __name__ == '__main__':
	main()