#  Define and code a function that, given a decimal number
# n whose digits are either zero or one, returns the number whose binary
# representation is precisely the sequence of zeros and ones in n. For
# example, if n = 10110_10 the function returns 22, since 10110_2 = 22.

def bin_to_dec(n):
	if n < 2:
		return n 
	else:
		return 2 * bin_to_dec(n // 10) + (n % 10)


def main():
	n = 10110
	print(n, bin_to_dec(n))


if __name__ == '__main__':
	main()

