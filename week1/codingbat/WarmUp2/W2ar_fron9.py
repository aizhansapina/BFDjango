def array_front9(nums):
  n = len(nums)
  if n > 4:
    n = 4
  for x in range(n):
    if nums[x] == 9:
      return True
  return False