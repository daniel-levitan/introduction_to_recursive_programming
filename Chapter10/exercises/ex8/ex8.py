# The function in Listing 10.9 counts the number of times that 
# two adjacent elements are identical in a list of length n ≥ 0.
# However, the method contains a bug. Find it and fix the function.

# I think the error is using lists with len less than 2

def count_consecutive_pairs(a):
	if len(a) < 2:
		return 0
	elif len(a) == 2:
		return int(a[0] == a[1])
	else:
		return int(a[0] == a[1]) + count_consecutive_pairs(a[1:])


def main():
	inputs = ['00', '1221', '122334', '12223', '1', '', '122344']

	for n in inputs:
		print(n, count_consecutive_pairs(n))


if __name__ == '__main__':
	main()