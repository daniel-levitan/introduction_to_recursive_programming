def count(t, i):
	if t == []:
		return 0
	else:
		return 1 + count(t[2], i) + count(t[3], i)


def main():
	T = ['Emma',
     '2002/08/23',
     ['Anna', '1999/12/03', [], []],
     ['Paul',
         '2000/01/13',
         ['Lara',
          '1987/08/23',
          ['John', '2006/05/08', [], []],
             ['Luke', '1976/07/31', [], []]],
         ['Sara', '1995/03/14', [], []]]]
	i = 0

	print(count(T, i))


if __name__ == '__main__':
	main()

