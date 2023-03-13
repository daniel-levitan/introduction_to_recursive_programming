# The code in Listing 10.10 computes the smallest prime factor of a number n, 
# which is greater than or equal to m. 

# The preconditions are: n ≥ m, n ≥ 2, and m ≥ 2. If it returns n when m = 2
# then n is a prime number. What problem will we encounter when trying
# to calculate the first 200 prime numbers?

# For the first 200 primes we've reached:
# RecursionError: maximum recursion depth exceeded in comparison
# We need to use dynamic programming to solve it

# Preconditions: n >= m, n >= 2, m >= 2
def smallest_prime_factor(n, m):
	if n % m == 0:
		return m
	else:
		return smallest_prime_factor(n, m + 1)



def main():
	
	m = 2
	n = 2
	k = 0
	while k < 201:
		p = smallest_prime_factor(n, m) 
		if p == n:
			k += 1
			print(k, p)
		n += 1



if __name__ == '__main__':
	main()