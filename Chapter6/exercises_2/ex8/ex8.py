# matrix mult =>   A * B = [A1  * [B1 | B2 ]  = [A1 * B1  A1 * B2]
#							--			 		 A2 * B1  A2 * B2
#                           A2]          
import numpy as np

def mult(A, B):
	p = A.shape[0]
	q = A.shape[1]
	r = B.shape[1]

	if p == 0 or q == 0 or r == 0:
		return np.zeros((p, q))
	elif p == 1 and r == 1:
		# return A * B
		# return np.matrix([[A[0, 0] * B[0, 0]]])
		summ = 0
		for i in range(len(A[0])):
			summ += A[0][i] * B.T[0][i]
		return np.array([[summ]])
	elif p == 1 and r != 1:
		b1 = B[:, :r // 2]
		b2 = B[:, r // 2:]
		c1 = mult(A, b1)
		c2 = mult(A, b2)
		return np.hstack([c1, c2])
	elif r == 1 and p != 1:
		a1 = A[:p // 2, :]
		a2 = A[p // 2:, :]
		c1 = mult(a1, B)
		c2 = mult(a2, B)
		return np.vstack([c1, c2])
	else:
		a1 = A[:p // 2, :]
		a2 = A[p // 2:, :]
		b1 = B[:, :r // 2]
		b2 = B[:, r // 2:]

		c11 = mult(a1, b1)
		c12 = mult(a1, b2)
		c21 = mult(a2, b1)
		c22 = mult(a2, b2)

		c1 = np.hstack([c11, c12])
		c2 = np.hstack([c21, c22])
		return np.vstack([c1, c2])


def main():
	A = np.array([[2, 3, 1, -3],
				   [4, -2, 1, 2]])

	B = np.array([[2, 3, 1],
				   [4, -1, -5],
    	           [0, -6, 3],
    	           [1, -1, 1]])
	print(mult(A, B))


	A = np.array([[1, 0], [2, 4]])
	B = np.array([[6, 8], [4, 3]])
	# [[6, 8], [28, 28]]
	print(mult(A, B))

	# A = np.matrix([[1]])
	# B = np.matrix([[2]])
	# print(mult(A, B))


if __name__ == '__main__':
	main()