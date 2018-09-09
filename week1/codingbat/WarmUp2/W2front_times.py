def front_times(str, n):
  res = ""
  front = 3
  if len(str) < front:
    front = len(str)

  for x in range(n):
    res = res + str[:front]
  return res