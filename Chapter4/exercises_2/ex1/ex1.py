def is_even(n):
	if n == 0:
		return True
	else:
		return not(is_even(n - 1))



def main():
	n = 4
	print(n, is_even(n))

	n = 7
	print(n, is_even(n))	


if __name__ == '__main__':
	main()