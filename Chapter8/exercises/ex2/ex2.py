# Almost fibonacci! Missing 0.

def rectangle(m, n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		return rectangle(m, n - 1) + rectangle(m, n - 2)


def main():
	m = 2
	# n = 10
	# print("n =", n, "", rectangle(m, n))

	for n in range(1, 11):
		print("n =", n, "", rectangle(m, n))


if __name__ == '__main__':
	main()

