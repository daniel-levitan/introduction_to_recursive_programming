# Rever

import math


def power_tail(b, n, s):
	if n == 0:
		return 1
	elif n == 1:
		return b * s
	else:
		return power_tail(b, n - 1, s * b);


def main():
	b = 2
	for n in range(1, 8):
		print(f"{b} to {n:d}  {int(math.pow(b, n)):3d}  {power_tail(b, n, 1):3d}")


if __name__ == '__main__':
	main()