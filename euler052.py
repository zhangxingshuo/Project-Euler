# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

import itertools as iter

def multPerm(n):
	perms = [int(''.join(i)) for i in [perm for perm in iter.permutations(str(n))]]
	for i in xrange(2,7):
		if i*n not in perms:
			return False
	return True

i = 1
while not multPerm(i):
	i += 1
print i