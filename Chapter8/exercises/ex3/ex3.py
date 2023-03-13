def scores(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	elif n == 3:
		return 4
	else:
		return scores(n - 1) + scores(n - 2) + scores(n - 3)


def main():
	for n in range(1, 10):
		print("Points =", n, "->",scores(n))


if __name__ == '__main__':
	main()
