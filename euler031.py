# In England the currency is made up of pound, lb, and pence, p, and there are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, lb1 (100p) and lb2 (200p).
# It is possible to make lb2 in the following way:

# 1xlb 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
# How many different ways can lb2 be made using any number of coins?

def coins(value):
	table = [0]*(value+1)
	table[0] = 1
	coinValues = [1,2,5,10,20,50,100,200]
	for coin in coinValues:
		for j in xrange(coin,value+1):
			table[j] += table[j-coin]
	return table[value]
print coins(200)