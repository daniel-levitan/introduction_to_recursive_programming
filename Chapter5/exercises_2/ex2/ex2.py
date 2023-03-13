# Represent a polynomial from a list
# [3, −5, 0, 1], corresponding to x3 − 5x1 + 3
# Highest order on the right

def represent(n):
	o = len(n) - 1

	if len(n) == 1:
		if n[0] >= 0:
			print("+", n[0], end = '')
		else:
			print("-", -n[0], end = '') 
	else:
		if n[-1] != 0:
			if n[-1] >= 0:
				print("+", n[-1], end = '')
			else:
				print("-", -n[-1], end = '')
			print("x^", end = '')
			print(o, end = ' ')

		represent(n[:-1])
	

def main():
	n = [3, -5, 0, 1]
	print(n)
	represent(n)
	print()
	

if __name__ == '__main__':
	main()

