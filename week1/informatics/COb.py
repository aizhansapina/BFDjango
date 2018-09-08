N = int(input())

if N % 4 != 0 or (N % 100 == 0 and N % 400 != 0):
	print("NO")
else:
	print("YES")
	
