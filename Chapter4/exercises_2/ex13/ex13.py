def factorial(n):
	if n == 0:
		return 0 
	else:
		return n * factorial(n - 1)


def binomial(n, m):
	if m == 0 or n == m:
		return 1 
	else:
		return binomial(n - 1, m - 1) + binomial(n - 1, m)



def binomial_n(n, m):
	if m == 0 or n == m:
		return 1 
	else:
		return n * binomial_n(n - 1, m) // (n - m)


def binomial_m(n, m):
	if m == 0 or n == m:
		return 1 
	else:
		return (n - m + 1) * binomial_m(n, m - 1) // m




def main():
	# print(1, binomial(0, 0))
	# print(1, binomial(1, 0))
	# print(1, binomial(1, 1))
	# print(2, binomial(2, 1))
	# print(3, binomial(3, 1))
	# print(4, binomial(4, 1))
	# print(6, binomial(4, 2))
	
	# print(1, binomial_n(0, 0))
	# print(1, binomial_n(1, 0))
	# print(1, binomial_n(1, 1))
	# print(2, binomial_n(2, 1))
	# print(3, binomial_n(3, 1))
	# print(4, binomial_n(4, 1))
	# print(6, binomial_n(4, 2))

	print(1, binomial_m(0, 0))
	print(1, binomial_m(1, 0))
	print(1, binomial_m(1, 1))
	print(2, binomial_m(2, 1))
	print(3, binomial_m(3, 1))
	print(4, binomial_m(4, 1))
	print(6, binomial_m(4, 2))


if __name__ == '__main__':
	main()