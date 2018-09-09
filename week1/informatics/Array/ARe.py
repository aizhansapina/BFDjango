import sys
a = []

N = int(input())
s = input()

a.append([int(x) for x in s.split()])
for x in range(1,N):
	if a[0][x] * a[0][x - 1]> 0:
		print("YES")
		sys.exit()
print("NO")