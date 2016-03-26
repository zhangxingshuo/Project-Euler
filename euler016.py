# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

def sumDigits(n):
	sum = 0
	while n > 0:
		sum += n%10
		n /= 10
	return sum

print sumDigits(2**1000)