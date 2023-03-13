def digits(n):
	if n < 10:
		return 1 
	else:
		return 1 + digits(n // 10)



def main():
	n = 12345
	print(len(str(n)), digits(n))

	n = 2222
	print(len(str(n)), digits(n))


if __name__ == '__main__':
	main()