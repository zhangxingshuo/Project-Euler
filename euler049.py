# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

import itertools as iter

#Sieve of Eratosthenes
def sieve(n):
	sieve = range(n + 1)
	sieve[1] = 0
	for i in xrange(2, int(round(n**0.5))):
		if sieve[i]:
			sieve[i*i: n+1: i] = [0] * len(xrange(i*i, n+1, i))
	return filter(None, sieve)

primes = sieve(10000)
primes = filter(lambda x: x > 999, primes)

def isPerm(primeTuple):
	perms = [int(''.join(digit)) for digit in [perm for perm in iter.permutations(str(primeTuple[0]))]]
	for i in primeTuple[1:]:
		if i not in perms:
			return False
	return True

L = []
for prime in primes:
	print prime
	for i in xrange(1,4500):
		if prime+i in primes and prime+2*i in primes:
			L.append((prime,prime+i,prime+2*i))
print filter(isPerm, L)