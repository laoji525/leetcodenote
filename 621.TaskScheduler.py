def tS(self, tasks, n):
	count = collections.Counter(tasks)
	m = max(count.values())
	res = ( m - 1 ) * ( n + 1)
	for k in count.values():
		if k == m:
			res += 1
	return max(res, len(tasks))
