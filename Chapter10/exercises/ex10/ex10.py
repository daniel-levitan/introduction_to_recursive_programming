# The code in Listing 10.11 pretends to compute the floor of a logarithm: 
# ⌊logb x⌋, where x ≥ 1 is a real number, and b ≥ 2 is an integer. 

# The idea consists of counting the number of times it is 
# possible to divide x by b. However, the code is incorrect. Find the bugs
# and modify the code in order to fix them.

# O erro era a divisão que deveria retornar inteiro e não float. Substituí / por //.

import math

def floor_log(x, b):
	if x == 1:
		return 0
	else:
		return 1 + floor_log(x // b, b)


def main():
	b = 2
	for n in range(1, 11):
		print(n, math.log(n, b), floor_log(n, b))
	
	# n = 7
	# print(floor_log(n, b))

	# print(math.log(2.7183, 2))
	# print(math.log(2, 2))
	# print(math.log(1, 2))



if __name__ == '__main__':
	main()