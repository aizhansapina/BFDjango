def max_end3(nums):
  large = max(nums[0], nums[len(nums) - 1])
  nums[0] = large
  nums[1] = large
  nums[2] = large
  
  return nums