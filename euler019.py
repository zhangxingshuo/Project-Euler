# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

days = [(1,1,1,1900)]

day = 1
month = 1
dayMonth = 1
year = 1900

while year != 2000 or month != 12 or dayMonth != 31:
	if day == 7:
		day = 0
	if dayMonth == 28 and month == 2 and (year%4 != 0 or (year%100 == 0 and year%400 != 0)):
		dayMonth = 0
		month += 1
	elif dayMonth == 29 and month == 2 and (year%4 == 0 or year%400 == 0):
		dayMonth = 0
		month += 1
	elif dayMonth == 30 and (month == 9 or month == 4 or month == 6 or month == 11):
		dayMonth = 0
		month += 1
	elif dayMonth == 31 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10):
		dayMonth = 0
		month += 1
	elif dayMonth == 31 and month == 12:
		dayMonth = 0
		month = 1
		year += 1
	dayMonth += 1
	day += 1
	days.append((day,dayMonth,month,year))

#print days

ans = filter(lambda x: x[0] == 7 and x[1] == 1 and x[3] > 1900, days)
print len(ans)