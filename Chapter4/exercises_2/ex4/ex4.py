def slow_product(m, n):
	if m == 1:
		return n
	else:
		return n + slow_product(m - 1, n)



def main():
	m, n = 3, 2
	print(m, n, slow_product(m, n))


	m, n = 3, 7
	print(m, n, slow_product(m, n))


if __name__ == '__main__':
	main()


