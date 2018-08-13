def lPS(self, s):
	if len(s) == 0: return ''
	start = 0
	maxlen = 1
	for i in range(len(s)):
		if i - maxlen >= 1 and s[i - maxlen -1: i + 1] == s[i - maxlen - 1: i + 1][::-1]:
			start = i - maxlen - 1
			maxlen += 2
			continue
		if i - maxlen >= 0 and s[i - maxlen: i + 1] == s[i - maxlen: i + 1][::-1]:
			start = i - maxlen
			maxlen += 1
	return s[start: start + maxlen]
