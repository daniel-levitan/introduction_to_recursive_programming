def ay(n):
	if n == 0:
		return True
	else:
		return not ay(n - 1)


def bee(n):
	if n == 0:
		return 3
	else:
		return n * bee(n - 1)


def cee(n):
	if n == 0:
		return 0
	else:
		return cee(n - 1) + 2 * n - 1

def dee(m, n):
	if m == 0 or n == 0:
		return 0
	else:
		return dee(m - 1, n - 1) + m + n - 1



def main():
	print("Test a")
	print("------")
	k = 5
	for n in range(0, k):
		print(n, ay(n))
	
	print()
	print("Test b")
	print("------")
	k = 5
	for n in range(0, k):
		print(n, bee(n))

	print()
	print("Test c")
	print("------")
	k = 5
	for n in range(0, k):
		print(n, cee(n))

	print()
	print("Test d")
	print("------")
	
	for m in [1, 5, 7, 8]:
		for n in [1, 5, 7, 8]:
			print(m, n, dee(m, n))


if __name__ == '__main__':
	main()