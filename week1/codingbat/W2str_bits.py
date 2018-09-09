def string_bits(str):
  res = ""
  n = len(str)
  for x in range(n):
   if x % 2 == 0:
     res = res + str[x]
  return res