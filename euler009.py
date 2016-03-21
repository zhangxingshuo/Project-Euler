#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.


def pyTriple():
	for a in xrange(1,500):
		for b in xrange(1,a):
			c = (a**2 + b**2)**0.5
			if c == int(round(c)) and a+b+c==1000:
					return int(a*b*c)
	return None

print(pyTriple())