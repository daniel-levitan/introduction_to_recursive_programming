import numpy as np

def transpose(m):
	p = m.shape[0]
	q = m.shape[1]
	
	if p == 1 and q == 1:
		return m
	else:

		m11 = transpose(m[0:p // 2, 0:q // 2])
		m21 = transpose(m[p // 2:p, 0:q // 2])
		m12 = transpose(m[0:p // 2, q // 2:q])
		m22 = transpose(m[p // 2:p, q // 2:q])

		return np.vstack([np.hstack([m11, m21]),
					      np.hstack([m12, m22])])		
	


def main():
	m = np.array([[1, 2], [3, 4]])
	print(m)
	print(transpose(m))

	A = np.array([[1, 2, 3, 4],
			   	  [5, 6, 7, 8],
				  [9, 10, 11, 12],
				  [13, 14, 15, 16]
				])
	print(A)
	print(transpose(A))

if __name__ == '__main__':
	main()