def string_match(a, b):
  cnt = 0
  short = 0
  n = len(a)
  m = len(b)
  
  if n < m:
    short = n
  if m < n:
    short = m
  if n == m:
    short = n
  
  for i in range(short - 1):
    for j in range(short - 1):
      if a[i] == b[j] and a[i + 1] == b[j + 1]:
        cnt += 1
  return cnt