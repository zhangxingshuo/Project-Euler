# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math

def digitFact(n):
	sum = 0
	while n > 0:
		sum += math.factorial(n%10)
		n //= 10
	return sum

digitFactL = filter(lambda x: x == digitFact(x), range(3,50000))
print sum(digitFactL)