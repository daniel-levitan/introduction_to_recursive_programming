def sum_iter(n, s):
	s = 0
	while n > 0:
		s += n 
		n -= 1

	return s


def sum_rec(s):
	if s == 1:
		return 1
	else:
		return s + sum_rec(s - 1)


def sum_tail(n, s):
	if n > 0:
		return sum_tail(n - 1, s + n) 
	else:
		return s 


def main():
	n = 4

	for n in range(1, 10):
		s = 0
		# print(sum_rec(n), sum_iter(n, s), sum_tail(n, s))
		print(f"{sum_rec(n):02d} {sum_iter(n, s):02d} {sum_tail(n, s):02d}")
		# print("{:02d} {:02d} {:02d}".format(sum_rec(n), sum_iter(n, s), sum_tail(n, s)))




if __name__ == '__main__':
	main()



