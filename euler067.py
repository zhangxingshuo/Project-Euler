def join(arr1,arr2):
	for i in range(len(arr1)):
		arr1[i] = arr1[i] + max(arr2[i],arr2[i+1])
	return arr1

f = open("triangle.txt","r")
arr = []
for line in f:
	arr.append([int(num) for num in line.split(' ')])


for i in xrange(len(arr) - 1):
	arr[len(arr)-i-2] = join(arr[len(arr)-i-2],arr[len(arr)-i-1])

print arr[0]