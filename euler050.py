# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

#Sieve of Eratosthenes
def sieve(n):
	sieve = range(n + 1)
	sieve[1] = 0
	for i in xrange(2, int(round(n**0.5))):
		if sieve[i]:
			sieve[i*i: n+1: i] = [0] * len(xrange(i*i, n+1, i))
	return filter(None, sieve)

primes = sieve(1000000)

def sumPrimes(lim):
	table = [0]*(lim+1)
	table[1] = 2
	for i in xrange(2,lim):
		table[i] = table[i-1] + primes[i-1]
	return  table

sumL = sumPrimes(10000)

max = 0
for i in xrange(1,len(sumL)):
	for j in reversed(xrange(1,len(sumL))):
		num = sumL[j] - sumL[i]
		if num in primes:
			if num > max:
				max = num
print max