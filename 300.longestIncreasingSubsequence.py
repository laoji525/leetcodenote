def lIS(self, nums):
	dp = [0] * len(nums)
	size = 0
	for x in nums:
		i, j = 0, size
		while i != j:
			m = (i + j) // 2
			if dp[i] < x:
				i = m + 1
			else:
				j = m
		dp[i] = x
		size = max(size, i + 1)
	return size
