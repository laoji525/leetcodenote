def mR1(self, intervals):
	d = collections.defaultdict(int)
	for k in intervals:
		for i in range(k.start, k.end):
			if d[i] == 0:
				d[i] = 1
			else:
				return False
	return True
	
