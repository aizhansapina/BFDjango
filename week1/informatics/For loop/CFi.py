a = int(input())
i = 0

for num in range(1, a + 1):
	if a % num == 0:
		i += 1
print(i)
		
