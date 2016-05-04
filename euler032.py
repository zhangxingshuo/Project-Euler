# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

def isPandigital(n):
	arr = sorted(map(int,str(n)))
	return arr == range(1,10)

def concat(num1,num2):
	return int(str(num1) + str(num2))

L = set([])

for i in xrange(2,100):
	for j in xrange(2,2000):
		product = i * j
		num = concat(concat(i,j),product)
		if isPandigital(num):
			L.update([product])

print sum(L)