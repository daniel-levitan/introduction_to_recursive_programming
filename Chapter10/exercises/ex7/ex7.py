# Eu acho que o erro est'ana função count digits. Quando representamos o número 0
# utilizamos um dígito, o digito 0. Logo, essa função deveria retornar 0 neste caso.
# A correção foi adicionada.


def add_digits(n):
	if n == 0:
		return 0
	# elif n < 10:
		# return n
	else:
		return add_digits(n // 10) + (n % 10)


def count_digits(n):
	# if n == 0:
		# return 0
	if n < 10:
		return 1
	else:
		return count_digits(n // 10) + 1


def main():
	inputs = [0, 1, 2, 12, 123, 1234]

	print("Add Digits:")
	for n in inputs:
		print(n, add_digits(n))

	print("Count Digits:")
	for n in inputs:
		print(n, count_digits(n))


if __name__ == '__main__':
	main()