# find the longest sublist with contiguous identical elements
# 

def is_equal(l):
	for i in range(1, len(l)):
		if l[0] != l[i]:
			return False
	return True


def is_equal_r(l):
	if len(l) == 1:
		return True
	else:
		return (l[0] == l[1]) and is_equal_r(l[1:])
	


def find(l):
	n = len(l)
	if is_equal(l):
		return l
	else:
		l_1 = find(l[1:n])
		l_2 = find(l[0:n - 1])
		if len(l_1) > len(l_2):
			return l_1
		else:
			return l_2


def main():
	a = [1, 3, 5, 5, 4, 4, 4, 5, 5, 6]
	print(find(a))
	
	# print(True, is_equal([1, 1, 1]))
	# print(False, is_equal([1, 2, 3]))

	# print(True, is_equal_r([1, 1, 1]))
	# print(False, is_equal_r([1, 2, 3]))


if __name__ == '__main__':
	main()