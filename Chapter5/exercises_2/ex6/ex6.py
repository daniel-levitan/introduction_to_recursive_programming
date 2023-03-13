# Write a function that searches for the item with the
# smallest key in a binary search tree T, defined as a list
# of four components

def find(t):
	if t[2] == []:
		return t[0]
	else:
		return find(t[2])




def main():

	t = ['Emma', '2002/08/23',
			['Anna', '1999/12/03', [], []],
			['Paul', '2000/01/13',
				['Lara', '1987/08/23',
					['John', '2006/05/08', [], []],
					['Luke', '1976/07/31', [], []]
				],
				['Sara', '1995/03/14', [], []]
			]
		]

	print(find(t))
	
if __name__ == '__main__':
	main()