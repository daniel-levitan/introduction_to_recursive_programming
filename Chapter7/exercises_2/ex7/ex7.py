def search_from_right(start, end, l):
	for i in range(end - 1, start, -1):
		if l[start] == l[i]:
			return i
	return []

def find(l, start, end):
	if len(l) == 0:
		return l
	elif start > end:
		return []
	else:
		e = search_from_right(start, end, l)
		if e:
			return [l[start]] + find(l, start + 1, e) + [l[start]]
		else:
			# return []
			return find(l, start + 1, end)

def main():
	#    0  1  2  3  4  5  6  7  8  9
	# a = [1, 3, 4, 4, 6, 3, 1, 5, 1, 3]
	# print([1, 3, 4, 4, 3, 1], find(a, 0, len(a)))

	#    0  1  2  3  4  5  6  7  8  9  0  1
	# a = [1, 7, 2, 8, 3, 2, 0, 0, 2, 1]
	# print([1, 2, 0, 0, 2, 1], find(a, 0, len(a)))


	# a = [1, 2, 2, 1, 6, 3, 1, 5, 2, 2, 1, 3]
	# print([1, 2, 2, 1, 1, 2, 2, 1], find(a, 0, len(a)))

	# a = [1, 2, 2, 1, 6, 3, 1, 5, 1, 3]
	# print([1, 2, 2, 1, 3, 1], find(a, 0, len(a)))



	# i = search_from_right(0, len(a), a)
	# print(i)

	# i = search_from_right(1, i, a)
	# print(i)

	# i = search_from_right(2, 5, a)
	# print(i)


if __name__ == '__main__':
	main()