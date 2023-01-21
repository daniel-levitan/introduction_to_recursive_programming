def fibonacci(n: int) -> int:
	if n == 1:
		return 1
	elif n == 2:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

def main():
	print(3, fibonacci(3))
	print(7, fibonacci(7))


# 1 1 2 3 5 8 13
if __name__ == '__main__':
	main()