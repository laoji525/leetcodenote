def mS(self, nums):
	if len(nums) == 0: return 0
	for i in range(1, len(nums)):
		if nums[i - 1] > 0:
			nums[i] += nums[i - 1]
	return max(nums)
