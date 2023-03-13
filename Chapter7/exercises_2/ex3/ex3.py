# Reference: https://medium.com/analytics-vidhya/understanding-recursion-with-factorial-and-an-english-ruler-drawing-7d1f8244a13a

# 0 to n inches
# every inch should be divided into 2^k
#   1     2     3     4
# 0   1/4   1/2   3/4   1
#      1     2     1     

# def print_parts(k, s, j):
# 	if s == 2 ** k:
# 		return
# 	else:
# 		if s < (2 ** k) // 2:
# 			print('-' * s)
# 		else:
# 			print('-' * ((2 ** k) - s))
# 		print_parts(k, s + 1, j + 1)

def draw_line(tick_length, tick_label=''):
	line = '-' * tick_length
	if tick_label:
		line += ' ' + tick_label
	print(line)


def draw_interval(center_length):
	if center_length > 0:
		draw_interval(center_length - 1)
		# draw_line(center_length)
		print('-' * center_length)
		draw_interval(center_length - 1)


def draw_ruler(n, major_length):
        draw_line(major_length, '0')
        for j in range(1, 1 + n):
            draw_interval(major_length - 1)
            draw_line(major_length, str(j))


def main():
	# draw_interval(2)
	draw_ruler(2, 3)
	# n = 2
	# k = 3
	# i = 0
	# j = 0
	# # print_ruler(n, k, 0)
	# print_parts(k, 1, j)
	# print()

if __name__ == '__main__':
	main()