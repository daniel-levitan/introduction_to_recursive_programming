def bits(n):
	if n == 1:
		return 1
	elif n == 2:
		return 4
	elif n == 3:
		return 11
	else:
		return bits(n - 1) + bits(n - 2) + bits(n - 3)


def main():
	n = 4
	print(n, bits(4))


if __name__ == '__main__':
	main()