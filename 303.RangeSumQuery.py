def _init_(self, nums):
	self.dp = nums
	for i in range(1, len(nums)):
		self.dp[i] += self.dp[i - 1]
	
	
def sumRange(self, i, j):
	return self.dp[j] - (self.dp[i - 1] if i > 0 else 0)
