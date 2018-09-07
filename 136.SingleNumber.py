def sN(self, nums):
	res = 0
	for d in nums:
		res ^= d
	return res
