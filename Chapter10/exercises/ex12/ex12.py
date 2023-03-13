# Consider a nonempty list a of n numbers that appear
# in increasing order until a certain index i (0 ≤ i ≤ n − 1), and then
# continue in decreasing order until the end of the list. The element ai,
# denoted as the “peak element,” and which we can consider to be unique,
# will therefore be the largest one on the list. The code in Listing 10.13
# tries to find this index, but contains an error. Find the bug and fix the
# function.

# O erro estava na segunda chamada de peak_element, o índice estava half e 
# assim entramos em recursão infinita

def peak_element(a, lower, upper):
	if lower == upper:
		return lower
	else:
		half = (lower + upper) // 2
		if a[half] > a[half + 1]:
			return peak_element(a, 0, half)
		else:
 			return peak_element(a, half + 1, upper)


def main():
	a = [1, 2, 3, 4, 4, 4, 4, 5]
	i = peak_element(a, 0, len(a) - 1)
	print(i, a[i])


if __name__ == '__main__':
	main()