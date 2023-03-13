def compute_wood(t, h):
	if t == []:
		return 0
	else:
		if t[0] > h:
			return t[0] - h + compute_wood(t[1:], h)
		else:
			return compute_wood(t[1:], h)


def wood_iter(trees, h):
	s = 0
	for t in trees:
		if t > h:
			s += t - h 
	return s


def wood_tail(trees, h, s):
	if len(trees) > 0:
		if trees[0] > h:
			return wood_tail(trees[1:], h, s + trees[0] - h)
		else:
			return wood_tail(trees[1:], h, s)
	else:
		return s


def main():
	trees = [5, 4, 3, 12, 8, 7, 5, 10, 7, 8, 4, 4, 11, 8, 7, 1, 9, 4, 3, 5]
	heights = [12, 11, 10, 9, 8, 7]

	for h in heights:
		s = 0
		print(f"h: {h:02d}", end="  ")
		print(f"rec: {compute_wood(trees, h):02d}", end="  ")
		print(f"iter: {wood_iter(trees, h):02d}", end="  ")
		print(f"tail: {wood_tail(trees, h, s):02d}")
	
	# print(f"{sum_rec(n):02d} {sum_iter(n, s):02d} {sum_tail(n, s):02d}")


if __name__ == '__main__':
	main()