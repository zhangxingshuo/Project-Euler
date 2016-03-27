# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

letterDict = {0:0,
1:3,
2:3,
3:5,
4:4,
5:4,
6:3,
7:5,
8:5,
9:4,
10:3,
11:6,
12:6,
13:8,
14:8,
15:7,
16:7,
17:9,
18:8,
19:8,
20:6,
30:6,
40:5,
50:5,
60:5,
70:7,
80:6,
90:6,
100:7,
1000:8}


def letterCount(n):
	if n == 1000:
		return letterDict[1] + letterDict[1000]
	elif n > 99 and n%100 > 19:
		return letterDict[n//100] + letterDict[100] + 3 + letterDict[n%100//10*10] + letterDict[n%10]
	elif n > 99 and n%100 < 20 and n%100 > 0:
		return letterDict[n//100] + letterDict[100] + 3 + letterDict[n%100]
	elif n > 99 and n%100 == 0:
		return letterDict[n//100] + letterDict[100]
	elif n < 100 and n > 19:
		return letterDict[n//10*10] + letterDict[n%10]
	else:
		return letterDict[n]

sum = 0
for i in xrange(1,1001):
	sum += letterCount(i)
print sum