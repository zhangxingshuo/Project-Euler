# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def sumDivisors(n):
	divL = [1]
	i = 2
	while i*i <= n:
		if n%i == 0 and i*i != n:
			divL.append(i)
			divL.append(n/i)
		elif i*i == n:
			divL.append(i)
		i+=1
	return sum(divL)

def abundant(n):
	if sumDivisors(n) > n:
		return True
	else:
		return False

lim = 28123

abundantL = filter(abundant, range(12,lim+1))
nonabundantSums = [False]*(lim+1)
for i in xrange(len(abundantL)):
	for j in xrange(i,len(abundantL)):
		abundantSum = abundantL[i] + abundantL[j]
		if abundantSum <= lim:
			nonabundantSums[abundantSum] = True

sum = 0
for i in xrange(lim+1):
	if not nonabundantSums[i]:
		sum += i
print sum