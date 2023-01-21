# sum_list_length_2
# Avoid using len

def sum_list_length_2(a):
	if a == []:
	# if not a: # This also works
		return 0
	else:
		return a[0] + sum_list_length_2(a[1:])


def main():
	a = [5, -1, 3, 2, 4, -3]
	print(sum_list_length_2(a))


if __name__ == '__main__':
	main()
