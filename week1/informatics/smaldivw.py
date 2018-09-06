n = int(input())
num = 2

while num < n and n > 2:
	num += 1
	if n % num == 0:
		print(num)
		break
	
