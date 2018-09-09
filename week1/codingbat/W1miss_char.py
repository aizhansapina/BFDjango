def missing_char(str, n):
  if len(str) > 1:
    return str[:n] + str[n+1:]