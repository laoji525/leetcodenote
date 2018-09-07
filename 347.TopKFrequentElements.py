def tKFE(self, nums, k):
	return [item[0] for item in collections.Counter(nums).most_common(k)]
