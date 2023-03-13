import numpy as np

def exists_path_swamp(A, r, c):
	if r < 0 or r >= A.shape[0] or A[r, c] == 'W':
		return False
	elif c == 1:
		return True
	else:
		return (exists_path_swamp(A, r - 1, c + 1)
				or exists_path_swamp(A, r, c + 1)
				or exists_path_swamp(A, r + 1, c + 1))


def main():
	A = np.matrix([['W', 'W', 'W', 'W', '·', '·', '·'],
    	           ['·', '·', 'W', '·', 'W', '·', 'W'],
        	       ['W', 'W', '·', '·', 'W', 'W', '·'],
            	   ['·', 'W', 'W', 'W', 'W', '·', 'W'],
               	   ['W', '·', '·', '·', 'W', 'W', 'W']])

	print(False, exists_path_swamp(A, 0, 0))
	print(True, exists_path_swamp(A, 1, 0))
	print(False, exists_path_swamp(A, 2, 0))
	print(False, exists_path_swamp(A, 3, 0))
	print(False, exists_path_swamp(A, 4, 0))
	print()



if __name__ == '__main__':
	main()