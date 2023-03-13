def shared(a):
	if len(a) == 1:
		return set(str(a[0]))
	elif len(a) == 2:
		return set(str(a[0])).intersection(set(str(a[1])))
	else:
		middle = len(a) // 2
		return shared(a[:middle]).intersection(shared(a[middle:]))

def main():
	a = [2348, 1349, 7523, 3215]
	# a = [2348, 1349, 7523, 3215, 2112]
	print(a, shared(a))



if __name__ == '__main__':
	main()