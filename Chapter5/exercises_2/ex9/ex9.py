def sqrt_root(a, x_n_minus_1, n):
	if n == 0:
		return x_n_minus_1
	else:
		x_n = x_n_minus_1 - ((x_n_minus_1 ** 2 - a) / (2 * x_n_minus_1))
		return sqrt_root(a, x_n, n - 1)


def main():
	a = 2
	x_0 = 1.1
	n = 10
	print(sqrt_root(a, x_0, n))


if __name__ == '__main__':
	main()