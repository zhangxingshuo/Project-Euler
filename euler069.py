# Euler's Totient function, phi(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, phi(9)=6.

# n	Relatively Prime	phi(n)	n/phi(n)
# 2	1	1	2
# 3	1,2	2	1.5
# 4	1,3	2	2
# 5	1,2,3,4	4	1.25
# 6	1,5	2	3
# 7	1,2,3,4,5,6	6	1.1666...
# 8	1,3,5,7	4	2
# 9	1,2,4,5,7,8	6	1.5
# 10	1,3,7,9	4	2.5
# It can be seen that n=6 produces a maximum n/phi(n) for n <= 10.

# Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.


# We want to maximize n/phi(n), which is maximizing n/n(prod(1-1/p)), where p is a unique prime factor of n.
# Thus, we want to minimize the denominator, which is finding a number with a large number of small primes.

import fractions

def totient(n):
	count = 0
	for k in xrange(1,n):
		if fractions.gcd(k,n) == 1:
			count += 1
	print count

#Sieve of Eratosthenes
def sieve(n):
	sieve = range(n + 1)
	sieve[1] = 0
	for i in xrange(2, int(round(n**0.5))):
		if sieve[i]:
			sieve[i*i: n+1: i] = [0] * len(xrange(i*i, n+1, i))
	return filter(None, sieve)

primes = sieve(200)
product = 1
i = 0
while product < 1000000:
	product *= primes[i]
	i += 1
print product/primes[i-1]