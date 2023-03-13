def find(l, x):
	if len(l) == 1:
		return l[0] == x
	else:
		middle = len(l) // 2
		if x == l[middle]:
			return True
		elif x < l[middle]:
			return find(l[:middle], x)
		else:
			return find(l[middle:], x)



def main():
	l = [1, 3, 5, 6, 7, 8, 9, 10]
	print(find(l, 3))
	print(find(l, 4))



if __name__ == '__main__':
	main()