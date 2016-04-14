# A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

def digitSum(n):
	sum = 0
	while n > 0:
		sum += n%10
		n //= 10
	return sum

max = 0
for a in xrange(1,101):
	for b in xrange(1,101):
		pow = digitSum(a**b)
		if pow > max:
			max = pow
print max