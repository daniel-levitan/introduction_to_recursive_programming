# n = 24667 and x = 5, the function should return 245667

def insert(n, x):
	if n == '':
		return x 
	else:
		if x <= n[0]:
			return x + n
		else:
			return n[0] + insert(n[1:], x)


def main():
	n = 24667
	x = 5
	print(int(insert(str(n), str(x))))


if __name__ == '__main__':
	main()