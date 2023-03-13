def binary_search(a, x, start):
	upper = len(a) - 1
	if len(a) < 1: # empty list
		return -1
	else:
		middle = len(a) // 2

		if x == a[middle]:
			return start + middle
		elif x < a[middle]:
			return binary_search(a[: middle - 1], x, start)
		else:
			return binary_search(a[middle + 1:], x, middle + 1)


def binary_search_wrapper(a, x):
	return binary_search(a, x, 0)


def main():
	l = [1, 1, 2, 3, 5, 7, 7, 8, 9]
	print(7, binary_search_wrapper(l, 8)) 
	print(2, binary_search_wrapper(l, 2))
	print(-1, binary_search_wrapper(l, 6))


if __name__ == '__main__':
	main()