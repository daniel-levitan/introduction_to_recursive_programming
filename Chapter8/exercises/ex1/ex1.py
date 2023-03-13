def variation(n, k):
	if k == 0:
		return 1
	else:
		return n * variation(n, k - 1)


def main():
	n = 4
	k = 2
	print(variation(n, k))


if __name__ == '__main__':
	main()