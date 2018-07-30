def mSAL(self, nums, k):
	m, s = 0, 0
	hashtable = {}
	for i in range(len(nums)):
		s += nums[i]
		diff = s - k
		if s == k:
			m = m + 1
		elif diff in hashtable:
			m = max(m, i - hashtable[diff])
		if s not in hashtable:
			hashtable[s] = i
	return m
