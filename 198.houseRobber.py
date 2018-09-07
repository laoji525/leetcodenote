def rob(self, nums):
	if not nums:
		return 0
	if len(nums) < 3:
		return max(nums)
	res = [nums[0], nums[1], nums[2] + nums[0]]
	for i in range(3, len(nums)):
		res.append(nums[i] + max(res[:i - 1]))
	return max(res)
