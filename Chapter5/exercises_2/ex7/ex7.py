def find(a, lower, upper):
	if lower > upper:
		return -1
	else:
		middle = (lower + upper) // 2
		if middle == a[middle]:
			return middle
		else:
			return max(
				find(a, lower, middle - 1),
				find(a, middle + 1, upper))
	

def main():
	a = [-3, -1, 2, 5, 6, 7, 9]
	print(find(a, 0, len(a) - 1))


if __name__ == '__main__':
	main()