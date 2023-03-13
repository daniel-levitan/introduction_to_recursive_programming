def C(n):
	if n == 0:
		return 1
	else:
		s = 0
		for i in range(0, n):
			s += C(i) * C(n - 1 - i)
		return s
		


def main():
	n = 6
	print(C(n))


if __name__ == '__main__':
	main()
