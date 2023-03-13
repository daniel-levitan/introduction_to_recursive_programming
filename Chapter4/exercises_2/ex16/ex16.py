# n = 24667 and x = 5, the function should return 245667

def insert(n, x):
	if n == []:
		return [x] 
	else:
		if x <= n[0]:
			return [x] + n
		else:
			return [n[0]] + insert(n[1:], x)


def main():
	n = [2, 4, 6, 6, 7]
	x = 5
	print(insert(n, x))


if __name__ == '__main__':
	main()