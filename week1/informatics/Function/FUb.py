def poww(a,b):
	if b == 0:
		return 1
	return a * poww(a, b - 1)

s = input()
a.append([float(x) for x in s.split()])

print(float(a[0][0] ** a[0][1]))