def sum_of_list_last(lst: list, size: int) -> int:
	if size == 0:
		return 0
	else:
		return sum_of_list_last(lst[:size - 1], size - 1) + lst[size - 1]


def sum_of_list_first(lst: list, size: int) -> int:
	if size == 0:
		return 0
	else:
		return lst[0] + sum_of_list_first(lst[1:], size - 1)


def sum_of_list_middle(lst: list, size: int) -> int:
	if size == 1:
		return lst[0]
	else:
		l = size // 2
		return sum_of_list_middle(lst[:l], len(lst[:l])) + sum_of_list_middle(lst[l:], len(lst[l:]))


def main():
	a = [5, -1, 3, 2, 4, -3]
	print(sum_of_list_last(a, len(a)))
	print(sum_of_list_first(a, len(a)))
	print(sum_of_list_middle(a, len(a)))


if __name__ == '__main__':
	main()