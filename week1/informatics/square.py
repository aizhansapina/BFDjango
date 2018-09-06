import math

a = int(input())
b = int(input())

for num in range (a, int(math.sqrt(b)) + 1):
	print(num * num, end = " ")
