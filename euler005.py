#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


#Note: this can be achieved simply through prime factorization, but that's too boring.

i = 1
for k in xrange(1,20):
	if i%k > 0:
		for j in xrange(1,20):
			if (i*j)%k == 0:
				i *= j
				break
print i