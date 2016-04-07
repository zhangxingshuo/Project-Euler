# The decimal number, 585 = (1001001001)2 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

def binary(n):
	return bin(n)[2:]

def isPalindrome(n):
	return str(n) == str(n)[::-1]

doublePalindrome = filter(lambda x: isPalindrome(x) and isPalindrome(binary(x)), range(1,1000000))

print sum(doublePalindrome)