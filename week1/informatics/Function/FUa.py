def minn(a,b,c,d):
	return min(min(a,b), min(c,d))
s = input()
a = []
a.append([int(x) for x in s.split()])

print(minn(a[0][0], a[0][1], a[0][2], a[0][3]))