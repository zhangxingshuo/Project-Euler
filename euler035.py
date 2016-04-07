# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

#Sieve of Eratosthenes
def sieve(n):
	sieve = range(n + 1)
	sieve[1] = 0
	for i in xrange(2, int(round(n**0.5))):
		if sieve[i]:
			sieve[i*i: n+1: i] = [0] * len(xrange(i*i, n+1, i))
	return filter(None, sieve)

primes = sieve(1000000)

def rotations(n):
	rotL = [n]
	string = str(n)
	string = string[1:] + string[0]
	while string != str(n):
		rotL.append(int(string))
		string = string[1:] + string[0]
	return rotL

def circular(n):
	if n in primes:
		rotL = rotations(n)
		for num in rotL:
			if num not in primes:
				return False
		return True
	else:
		return False

circularD = {}
for prime in primes:
	circularD[prime] = False

for key in circularD:
	if not circularD[key]:
		if circular(key):
			rotL = rotations(key)
			for num in rotL:
				circularD[num] = True

circularL = filter(lambda x: circularD[x], primes)
print len(circularL)