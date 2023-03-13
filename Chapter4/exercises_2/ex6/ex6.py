def efe_i(i):
	return i ** 3

def summ(m, n, f):
	if n < m:
		return f(m) 
	else:
		return f(m) + summ(m + 1, n, f)


def main():
	m = 0 

	for n in range(0, 5):
		print(n, summ(m, n, efe_i))


if __name__ == '__main__':
	main()