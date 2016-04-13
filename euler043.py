# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

#Sieve of Eratosthenes
def sieve(n):
	sieve = range(n + 1)
	sieve[1] = 0
	for i in xrange(2, int(round(n**0.5))):
		if sieve[i]:
			sieve[i*i: n+1: i] = [0] * len(xrange(i*i, n+1, i))
	return filter(None, sieve)

primes = sieve(18)

import itertools as iter

pandigital = [int(''.join(i)) for i in [perm for perm in iter.permutations("0123456789")]]

def subDiv(num):
	for i in xrange(1,8):
		if int(str(num)[i:i+3]) % primes[i-1] != 0:
			return False
	return True

# print subDiv(1406357289)
print sum(filter(subDiv,pandigital))
