def bool_binary_search(a, x):
	if len(a) == 0:
		return False
	else:
		middle = (len(a) - 1) // 2

		if a[middle] == x:
			return True
		elif x < a[middle]:
			return bool_binary_search(a[: middle - 1], x)
		else:
			return bool_binary_search(a[middle + 1:], x)



def main():
	a = [1, 3, 6, 7, 8, 12]
	x = 5
	print(x, bool_binary_search(a, x))

	x = 8
	print(x, bool_binary_search(a, x))


if __name__ == '__main__':
	main()