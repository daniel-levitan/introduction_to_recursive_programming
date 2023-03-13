import pprint

def towers_of_Hanoi(T, n, o, d, a):
	x = "Disk: " + str(n) + " " +\
	    "o:" + str(o) + " " +\
	    "d:" + str(d) + " " + \
	    "a:" + str(a)
	insert_tree(x, T)
	if n == 1:
		print('Move disk', n, 'from rod', o, 'to rod', d)
	else:
		towers_of_Hanoi(T, n - 1, o, a, d)
		print('Move disk', n, 'from rod', o, 'to rod', d)
		towers_of_Hanoi(T, n - 1, a, d, o)


def insert_tree(x, T):
	if T == []:
		T.extend([x, []])
	else:
		if T[1] == []:
			T[1] = [x, []]
		else:
			insert_tree(x, T[1])
			

def main():
	T = []
	towers_of_Hanoi(T, 4, 'O', 'D', 'A')
	
	# print(T)
	pprint.pprint(T)

if __name__ == '__main__':
	main()