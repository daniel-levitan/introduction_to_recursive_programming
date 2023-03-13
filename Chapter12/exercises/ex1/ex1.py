# Inclusion/exclusion patter
def listSubsets(inp, soFar, subsets):
	if inp == '':
		# print(soFar)
		subsets.append(soFar)
	else:
		consider = inp[0]
		rest = inp[1:]
		listSubsets(rest, soFar + consider, subsets)
		listSubsets(rest, soFar, subsets)


# Backtracking
def explore(i, options, soFar, subsets):
	subsets.append(soFar[:])
	for k in range(i, len(options)):
		soFar.append(options[k])
		explore(k + 1, options, soFar, subsets)
		soFar.pop()


# Backtracking
def dfs(options, index, path, result):
	result.append(path)
	for i in range(index, len(options)):
		dfs(options, i + 1, path + [options[i]], result)


def main():

	# subsets = []
	# listSubsets('012', '', subsets)
	# print(subsets)

	subsets = []
	explore(0, [0, 1, 2], [], subsets)
	print(subsets)

	# result = []
	# dfs([0, 1, 2], 0, [], result)
	# print(result)


if __name__ == '__main__':
	main()