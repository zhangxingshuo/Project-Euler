# Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

# Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

# We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

# Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

# Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

# Find the least number for which the proportion of bouncy numbers is exactly 99%.

def inc(n):
	s = str(n)
	max = int(s[-1])
	for char in s[::-1]:
		if int(char) > max:
			return False
		max = int(char)
	return True

def dec(n):
	s = str(n)
	min = int(s[-1])
	for char in s[::-1]:
		if int(char) < min:
			return False
		min = int(char)
	return True

def bouncy(n):
	if not inc(n) and not dec(n):
		return True
	else:
		return False

#bouncyL = filter(bouncy,range(5000000))
#print 1.0*len(bouncyL)/5000000

#bouncyL = filter(bouncy,range(539))
#print 1.0*len(bouncyL)/538

bouncyL = filter(bouncy,range(1000000))
bouncyCount = len(bouncyL)
i = 999999
while 1.0*bouncyCount/i < 0.99:
	if bouncy(i+1):
		bouncyCount += 1
	i += 1
print i