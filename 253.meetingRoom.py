def mR1(self, intervals):
	d = collections.defaultdict(int)
	for k in intervals:
		for i in range(k.start, k.end):
			if d[i] == 0:
				d[i] = 1
			else:
				return False
	return True


#better solution
def mR2(self, intervals):
	intervals.sort(key = lambda x : x.start)
	for i, k in enumerate(intervals, 1):
		if k.start < intervals[i - 1]:
			return False
	return True
