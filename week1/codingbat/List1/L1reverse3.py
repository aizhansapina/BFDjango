def reverse3(nums):
  num0 = nums[0]
  nums[0] = nums[2]
  nums[2] = num0
  
  return nums