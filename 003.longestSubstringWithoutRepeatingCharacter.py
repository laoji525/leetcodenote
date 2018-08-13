def lSWRC(self, s):
	l_s = {}
	start, longest = 0, 0
	for i, c in enumerate(s):
		if c in l_s and l_s[c] >= start:
			start = l_s[c] + 1
		else:
			longest = max(longest, i - start + 1)
		l_s[c] = i
	return longest
