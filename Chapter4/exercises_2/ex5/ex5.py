def less_slow_product(m, n):
	if m == 1:
		return n 
	elif n == 1:
		return m 
	else:
		if m % 2 == 0 and n % 2 == 0:
			return less_slow_product(m // 2, n // 2) * 4
		elif m % 2 == 0 and n % 2 != 0:
			return less_slow_product(m // 2, n // 2) * 4 + n - 1
		elif m % 2 != 0 and n % 2 == 0:
			return less_slow_product(m // 2, n // 2) * 4 + m - 1
		else:
			return less_slow_product(m // 2, n // 2) * 4 + m + n - 1


def main():
	m, n = 5, 7
	print(m, n, less_slow_product(m, n))


if __name__ == '__main__':
	main()