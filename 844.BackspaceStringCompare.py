def backspaceCompare(self, S, T):
	ss = []
	tt = []
	for s in S:
		if s == '#':
			if ss:
				ss.pop()
		else:
			ss.append(s)
	for c in T:
		if c == '#':
			if tt:
				tt.pop()
		else:
			tt.append(c)
	return ss == tt
