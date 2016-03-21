#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?


#unnecesssary prime number test, but maybe useful in the future
def isPrime(n):
	if n==1 or n==0: 
		return False
	else:
		for i in xrange(2,int(round(n^(1/2)))):
			if n%i ==0:
				return False
		return True

def primeFactors(n):
	factors = []
	i = 2
	while i*i <= n:
		if n%i:
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return factors

print primeFactors(600851475143)[-1]