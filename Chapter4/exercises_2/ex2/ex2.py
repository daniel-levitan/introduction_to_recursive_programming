def power(b, n):
	if n == 0:
		return 1
	elif n == 1:
		return b
	elif n > 0:
		if n % 2 == 0:
			return power(b, n // 2) ** 2
		else:
			return b * power(b, n // 2) ** 2
	else:
		if n % 2 == 0:
			return 1 / (power(b, -n // 2) ** 2)
		else:
			return 1 / (b * power(b, -n // 2) ** 2)

def main():
	# b, n = 2, 3
	# print(b, n, power(b, n))

	# b, n = 2, 4
	# print(b, n, power(b, n))

	# b, n = 2, 1
	# print(b, n, power(b, n))	

	# b, n = 1, 3
	# print(b, n, power(b, n))

	# b, n = -2, 3
	# print(b, n, power(b, n))

	b, n = 2, -3
	print(b, n, power(b, n))


if __name__ == '__main__':
	main()
