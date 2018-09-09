def front_back(str):
  n = len(str)
  if len(str) <= 1:
    return str
  if len(str) > 1:
    return str[n -1] + str[1:n-1] + str[0]