a = []

N = int(input())
s = input()

res = 0
a.append([int(x) for x in s.split()])
for x in range(0,N):
	if a[0][x] > a[0][x - 1]:
		res = res + 1
print(res)