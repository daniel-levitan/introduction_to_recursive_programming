def count_els(a, b):
	if len(a) == 0:
		return
	else:
		d = a[0]
		b[d] += 1
		return count_els(a[1:], b)


def sort_els(b):
	d = len(b) - 1
	
	if len(b) == 0:
		return []
	else:
		c = []
		while b[d] > 0:
			c.append(d)
			b[d] -= 1
		return sort_els(b[:-1]) + c




def main():
	a = [2, 2, 3, 2, 0, 1, 3, 2, 0, 0, 4]
	b = [0, 0, 0, 0, 0]
	
	count_els(a, b)
	print(b)
	
	# b = [3, 1, 2] # [0, 0, 0, 1, 2, 2]

	print(sort_els(b))
	

if __name__ == '__main__':
	main()