# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?

def pandigital(n,num):
	digits = range(1,n+1)
	string = [int(i) for i in list(str(num))]
	for digit in digits:
		try:
			string.remove(digit)
		except ValueError:
			return False
	if string == []:
		return True
	else:
		return False

#Sieve of Eratosthenes
def sieve(n):
	sieve = range(n + 1)
	sieve[1] = 0
	for i in xrange(2, int(round(n**0.5))):
		if sieve[i]:
			sieve[i*i: n+1: i] = [0] * len(xrange(i*i, n+1, i))
	return filter(None, sieve)

primes = sieve(10000000)

max = 0
for i in xrange(1,10):
	print i
	for prime in primes:
		if pandigital(i,prime) and prime > max:
			max = prime

print max