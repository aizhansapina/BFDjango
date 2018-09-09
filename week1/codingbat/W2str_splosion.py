def string_splosion(str):
  res = ""
  n = len(str)
  
  for x in range(n + 1):
    res = res + str[:x] 
  return res