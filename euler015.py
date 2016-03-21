#Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

#How many such routes are there through a 20x20 grid?

def latticePath(down,right,cache={}):
	if (down, right) not in cache:
		if down == 0 or right == 0:
			cache[(down,right)] = 1
		else:
			cache[(down,right)] = latticePath(down-1,right) + latticePath(down,right-1)
	return cache[(down,right)]

print latticePath(20,20)