# https://math.stackexchange.com/questions/3326027/how-to-prove-that-number-of-unlabelled-binary-trees-n-nodes-is-given-by-catala
# So our tree has a root and a left child and a right child. (If a child doesn't exist, I will consider it a child with zero nodes.)

# Suppose that the left child is the root of a tree with 𝑖 nodes. 
# Then the right child would have to be the root of a tree with 𝑛−𝑖−1 nodes, since the
# total of the nodes in those two trees plus the root of our tree must equal 𝑛. 

# We've decided that there are 𝐹(𝑖) possible trees that can be made from 𝑖 nodes 
# to be rooted at the left child and 𝐹(𝑛−𝑖−1) possible trees that can be made 
# rooted at the right child. So the total number of rooted trees that have 𝑖
# nodes on the left and 𝑛−𝑖−1 nodes on the right is 𝐹(𝑖)𝐹(𝑛−𝑖−1).

# Of course, the number of nodes on the left side can vary anywhere from 0 to 𝑛−𝑖−1
# nodes, so the grand total number of rooted trees with 𝑛 vertices is
# 𝐹(𝑛)=∑𝑖=0𝑛−1𝐹(𝑖)𝐹(𝑛−𝑖−1).
# To give us an initial point for this recursion, we note that there is only 
# one binary tree with zero nodes (the empty tree), so 𝐹(0)=1.
#
# Another source: https://www.whitman.edu/mathematics/cgt_online/book/section03.05.html

def bin(n):
	if n == 0:
		return 1
	else:
		s = 0
		for i in range(0, n):
			s += bin(i) * bin(n - 1 - i)
		return s


def main():
	for n in range(0, 6):
		print("n =", n, " ->", bin(n))


if __name__ == '__main__':
	main()