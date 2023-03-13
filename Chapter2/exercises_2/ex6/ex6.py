def find_largest(n, largest):
	if largest == 0:
		largest = n[0]

	if len(n) == 0:
		return largest
	else:
		if n[0] > largest:
			largest = n[0]
		return max(largest, find_largest(n[1:], largest))


def main():
	l = [1, 7, 3, 6, 4, 2, 5]
	print(find_largest(l, 0))


if __name__ == '__main__':
	main()
