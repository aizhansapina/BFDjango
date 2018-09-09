def array123(nums):
  n = len(nums)
  for x in range(n - 2):
    if nums[x] == 1 and nums[x + 1] == 2 and nums[x + 2] == 3:
      return True
  return False