import pprint

def insert_binary_tree(x, T):
	if T == []:
		T.extend([x[0], x[1], [], []])
	else:
		if x[0] < T[0]:
			if T[2] == []:
				T[2] = [x[0], x[1], [], []]
			else:
				insert_binary_tree(x, T[2])
		else:
			if T[3] == []:
				T[3] = [x[0], x[1], [], []]
			else:
				insert_binary_tree(x, T[3])


def main():
	a = [('John', '2006/05/08'),('Luke', '1976/07/31'), 
		 ('Lara', '1987/08/23'), ('Sara', '1995/03/14'),
		 ('Paul', '2000/01/13'), ('Anna', '1999/12/03'), 
		 ('Emma', '2002/08/23')]
	T = []

	# Essa função reproduz a figura 5.2 na qual a lista é criada a partir 
	# do primeiro elemento
	for item in a:
		insert_binary_tree(item, T)
	pprint.pprint(T)


	# Essa aqui cria a lista a partir do último elemento
	for item in reversed(a):
		insert_binary_tree(item, T)
	pprint.pprint(T)	

	


if __name__ == '__main__':
	main()