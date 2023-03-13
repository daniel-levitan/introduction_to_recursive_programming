def decimal_to_binary(n):
	if n < 2:
		return n
	else:
		return 10 * decimal_to_binary(n // 2) + (n % 2)


def generate(n):
	i = 1
	b = decimal_to_binary(i)
	result = []

	while len(str(b)) < n + 1:
		result.append(b)
		i += 1
		b = decimal_to_binary(i)

	return result


def count(n, i, total):
	if 2 ** n - 1 < i:
		return total
	else:
		b = decimal_to_binary(i)
		total += pos(b)
		print(b, total)
		return count(n, i + 1, total)
		

def pos(n):
	if n % 10 == 1:
		return 1 
	else:
		return 1 + pos(n // 10)


def main(): 
	total = 0
	print(count(4, 1, total))

	



if __name__ == '__main__':
	main()