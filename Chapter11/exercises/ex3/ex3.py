def add(l):
	if l == []:
		return 0 
	else:
		return l[0] + add(l[1:])


def add_tail(l, s):
	if l != []:
		return add_tail(l[1:], s + l[0])
	else:
		return s


def add_iter(l):
	s = 0

	while l != []:
		s += l[0]
		l = l[1:]

	return s

def main():
	l = [1, 4, 5, 6, 8, 3, 2]
	s = 0
	print(f"rec: {add(l):2d}   tail: {add_tail(l, s):2d}   iter: {add_iter(l):2d}")

if __name__ == '__main__':
	main()