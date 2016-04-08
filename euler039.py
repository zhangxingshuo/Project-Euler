# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p <= 1000, is the number of solutions maximised?

def triangle(perimeter):
	L = []
	for a in xrange(perimeter/2):
		for b in xrange(a):
			c = perimeter - b - a
			if a**2 + b**2 == c**2:
				L.append((a,b,c))
	return L

max = 0
index = 0
for i in xrange(12,1000):
	tri = len(triangle(i))
	if tri > max:
		max = tri
		index = i
print index