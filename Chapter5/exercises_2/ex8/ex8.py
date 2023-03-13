
def find(a, lower, upper):
	if lower > upper:
		return -1
	else:
		middle = (lower + upper) // 2

		if a[middle] % 2 == 0:
			return max(middle, find(a, middle + 1, upper))
		else:
			return find(a, lower, middle - 1)


def main():
	a = [2, -4, 10, 8, 0, 12, 9, 3, -15, 3, 1]
	print(find(a, 0, len(a) - 1))


if __name__ == '__main__':
	main()