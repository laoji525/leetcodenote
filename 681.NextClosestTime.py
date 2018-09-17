def	nextClosestTime(self, time):
	allow = set([s for s in time if s != ':'])
	front = int(time[:2])
	back = int(time[3:])
	t = front * 60 + back
	nt = t + 1
	while nt != t:
		if nt >= 1440:
			nt -= 1440
		front = nt // 60
		back = nt % 60
		f = str(front)
		if front < 10:
			f = '0' + f
		if back < 10:
			b = '0' + b
		if all(c in allow for c in f + b):
			return f + ':' + b
		nt += 1
	return time
