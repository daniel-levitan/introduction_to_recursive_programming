import math

def fib_linear(n):
	if (n == 1) or (n == 2):
		return 1
	else:
		golden_ratio = (1 + math.sqrt(5)) / 2
		return math.floor(golden_ratio * fib_linear(n - 1) + 1 / 2)


def fib_tail(n, a, b):
	if n == 1:
		return b
	else:
		return fib_tail(n - 1, a + b, a)


def fib_tail_wrapper(n):
	return fib_tail(n, 1, 1)


def fib_multiple(n):
	if n == 1 or n == 2:
		return 1
	elif n > 2 and n % 2 == 0:
		return fib_multiple(n / 2 + 1) ** 2 - fib_multiple(n / 2 - 1) ** 2
	else:
		return fib_multiple((n + 1) / 2) ** 2 + fib_multiple((n - 1) / 2) ** 2


def fib_mutual_A(n):
	if n == 1:
		return 0
	else:
		return fib_mutual_A(n - 1) + fib_mutual_B(n - 1)


def fib_mutual_B(n):
	if n == 1:
		return 1
	else:
		return fib_mutual_A(n - 1)


def fib_mutual_wrapper(n):
	return fib_mutual_B(n) + fib_mutual_A(n)


def fib_nested(n, s):
	if n == 1 or n == 2:
		return 1 + s
	else:
		return fib_nested(n - 1, s + fib_nested(n - 2, 0))


def fib_nested_wrapper(n):
	return fib_nested(n, 0)


def main():
	for f in [fib_linear, fib_tail_wrapper, fib_multiple, fib_mutual_wrapper, fib_nested_wrapper]:
		print(str(f))
		for i in range(1, 11):
			print(f(i))
	

if __name__ == '__main__':
	main()