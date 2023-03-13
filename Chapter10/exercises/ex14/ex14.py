def bin(D, n, m):
	if m == 0 or n == m:
		D[n][m] = 1
		return D[n][m]
	elif D[n][m] > -1:
		return D[n][m]
	else:
		D[n][m] = bin(D, n - 1, m - 1) + bin(D, n - 1, m)
		return D[n][m]


def main():
	# n must be greater than m
	n = 70
	m = 10


	D = [[-1 for i in range(m + 1)] for j in range(n + 1)]
	# print(D)

	print("n:",n, " m:", m, "binome:", bin(D, n, m))


if __name__ == '__main__':
	main()