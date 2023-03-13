# For example, if the input is [1, 3, 3, 1] the result should be [4, 6, 4].

def summ(l, r, i):
	if i > len(l) - 2:
		return r 
	else:
		r.append(l[i] + l[i + 1])
		return summ(l, r, i + 1)


def main():
	l = [1, 3, 3, 1]
	r = []
	i = 0
	
	print(summ(l, r, i))


if __name__ == '__main__':
	main()

