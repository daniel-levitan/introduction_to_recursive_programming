# def get_max(l):
# 	result = []
# 	maxx = l[0]
# 	for i in range(len(l)):
# 		if maxx + l[i] >= maxx:
# 			result.append(l[i])
# 			maxx += l[i]
# 		else:
# 			break
# 	return result
#
#
# def get_max_list(l):
# 	maxx = None
# 	for i in range(len(l)):
# 		if maxx == None:
# 			maxx = l[i]
# 			if get_max(l[i:])


def expand_left(l):
	maxx = l[-1]
	result = []
	for i in range(len(l) - 1, -1, -1):
		if maxx + l[i] >= maxx:
			result = [l[i]] + result
			maxx += l[i]
		else:
			break
	return result


def expand_right(l):
	maxx = l[0]
	result = [l[0]]
	for i in range(1, len(l)):
		if maxx + l[i] >= maxx:
			result.append(l[i])
			maxx += l[i]
		else:
			break
	return result


def get_sublist(l):
	if len(l) == 0:  # Is this necessary?
		return []
	elif len(l) == 1:
		return l
	else:
		middle = len(l) // 2
		left_sl = l[:middle]
		right_sl = l[middle:]

		mid_sl = expand_left(l[:len(l) // 2]) + expand_right(l[len(l) // 2:])

		if sum(left_sl) >= sum(right_sl):
			if sum(left_sl) > sum(mid_sl):
				return left_sl
			else:
				return mid_sl
		else:
			if sum(right_sl) > sum(mid_sl):
				return right_sl
			else:
				return mid_sl


def main():
	l = [-1, -4, 5, 2, -3, 4, 2, -5]
	print(get_sublist(l))

	l = [1, 2, 5, 2, -3, -4, 2, -5]
	print(get_sublist(l))



if __name__ == '__main__':
		main()	