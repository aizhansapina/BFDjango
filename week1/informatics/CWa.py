import math
N = int(input())
num = 0
while num < int(math.sqrt(N)) :
	num += 1
	print(num * num)
