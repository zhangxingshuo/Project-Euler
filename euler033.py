# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

def factors(n):
	divL = [1,n]
	i = 2
	while i*i <= n:
		if i*i == n:
			divL.append(i)
		elif n%i == 0:
			divL.append(i)
			divL.append(n/i)
		i+=1
	return sorted(divL)

def simplify(num,den):
	gcd = max(set(factors(num)) & set(factors(den)))
	if gcd == 1:
		return num, den
	else:
		return simplify(num/gcd, den/gcd)

def join(L):
	if len(L) > 0:
		s = ''.join(map(str,L))
		return int(s)
	else:
		return 0

def badSimplify(num,den):
	numL, denL = list(str(num)), list(str(den))
	common = list(set(numL) & set(denL))
	for elem in common:
		numL.remove(elem)
		denL.remove(elem)
	return join(numL), join(denL)

L = []
for den in xrange(1,99):
	for num in xrange(1,den):
		simp = simplify(num,den)
		badSimpNum, badSimpDen = badSimplify(num,den)
		badSimp = simplify(badSimpNum,badSimpDen)
		if simp == badSimp and (num,den) != simp and (num,den) != (badSimpNum,badSimpDen):
			L.append((num,den))

L = filter(lambda x: x[0] % 10 != 0 and x[0] != x[1],L)

numProd = 1
denProd = 1

for frac in L:
	numProd *= frac[0]
	denProd *= frac[1]

print simplify(numProd, denProd)