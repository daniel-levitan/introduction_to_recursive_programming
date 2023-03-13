# Consider a list a of n numbers. We say that it contains a “greatest” element 
# if one of the entries of the list is greater than the sum of all of the rest.

# Ele nunca chegava ao caso recursivo

def contains_greatest_element(a):
	# if a == []:
		# return False
	if len(a) == 1:
		return False
	else:
		return (2 * a[0] > sum(a) or contains_greatest_element(a[1:]))
		# return (2 * a[0] > sum(a) or contains_greatest_element(a[1:]))


def main():
	a = [4, 1, 1, 1]
	a = [1, 4, 1, 1]
	print(contains_greatest_element(a))
	

if __name__ == '__main__':
	main()
