a = []

N = int(input())
s = input()

a.append([int(x) for i in s.split()])
for i in range(0, N):
	if a[0][i] % 2 == 0:
		print(a[0][i], end = " ")