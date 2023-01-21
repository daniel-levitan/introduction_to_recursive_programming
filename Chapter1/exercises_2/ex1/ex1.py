def func(n: int) -> int:
	if n == 0:
		return 1
	else:
		return func(n - 1) * n


def main():
	print(6, func(6))
	print(3, func(3))


if __name__ == '__main__':
	main()