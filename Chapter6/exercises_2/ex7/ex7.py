# matrix mult =>   A * B = [A1 | A2] * [B1    = [A1 * B1 + A2 * B2]
#										---
#										B2 ]
import numpy as np

def mult(A, B):
	p = A.shape[1]
	q = B.shape[0]

	if p == 0 or q == 0:
		return np.zeros((p, q))
	elif p == 1 and q == 1:
		return np.matrix([[A[0, 0] * B[0, 0]]])
	else:
		a1 = A[:,:p // 2]
		a2 = A[:,p // 2:]
		b1 = B[:q // 2, :]
		b2 = B[q // 2:, :]

		c1 = mult(a1, b1)
		c2 = mult(a2, b2)

		return np.array(c1 + c2)


def main():
	A = np.matrix([[2, 3, 1, -3], 
				   [4, -2, 1, 2]])

	B = np.matrix([[2, 3, 1], 
				   [4, -1, -5],
    	           [0, -6, 3], 
    	           [1, -1, 1]])

	print(mult(A, B))

	# A = np.matrix([[1]])
	# B = np.matrix([[2]])
	# print(mult(A, B))


if __name__ == '__main__':
	main()