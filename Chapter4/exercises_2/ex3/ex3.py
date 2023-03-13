import numpy as np 

def matrix_power(m, n):
	if n == 1:
		return m.dot(np.identity(m.shape[0]))
	else:
		return m.dot(matrix_power(m, n - 1))


def main():
	m = np.matrix([[1, 1], [1, 0]])
	for i in range(1, 11):
		print(i, matrix_power(m, i)[0, 1])


if __name__ == '__main__':
	main()

