
def pos(n):
	if n % 10 == 1:
		return 1 
	else:
		return 1 + pos(n // 10)


def main(): 
	n = 1110100
	print(n, pos(n))

	n = 101
	print(n, pos(n))

	n = 110
	print(n, pos(n))



if __name__ == '__main__':
	main()