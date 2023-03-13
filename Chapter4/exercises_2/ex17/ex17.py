def insert(n, x):
	if n == []:
		return [x] 
	else:
		if x <= n[0]:
			return [x] + n
		else:
			return [n[0]] + insert(n[1:], x)


def insertion_sort(l, i):
	if i > len(l) - 1:
		return l
	else:
		r = insert(l[:i], l[i])
		return insertion_sort(r + l[i + 1:], i + 1)



def main():
	l = [1, 3, 5, 5, 6, 4, 2, 8, 1, 9, 3, 7, 8]
	print(insertion_sort(l, 1))


if __name__ == '__main__':
	main()