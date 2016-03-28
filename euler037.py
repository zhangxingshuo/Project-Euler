# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

#Sieve of Eratosthenes
def sieve(n):
	sieve = range(n + 1)
	sieve[1] = 0
	for i in xrange(2, int(round(n**0.5))):
		if sieve[i]:
			sieve[i*i: n+1: i] = [0] * len(xrange(i*i, n+1, i))
	return filter(None, sieve)

primes = sieve(1000000)

def rTruncate(n):
	while n > 0:
		if n not in primes:
			return False
		n //= 10
	return True

def lTruncate(n):
	while n > 0:
		if n not in primes:
			return False
		n %= 10**(len(str(n))-1)
	return True

sum = 0
count = 0
for prime in primes[4:]:
	print prime
	if rTruncate(prime) and lTruncate(prime):
		sum += prime
		count += 1
print count, sum