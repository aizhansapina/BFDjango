a = []
N = int(input())
arr = input()

a.append([int(x) for x in arr.split()])
for x in range(0, N):
	if x % 2 == 0:
		print(a[0][x])