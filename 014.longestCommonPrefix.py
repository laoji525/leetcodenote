def lCP(self, strs):
	if not strs: return ''
	p = ''
	shortest = min(strs, key=len)
	for i in range(len(shortest)):
		for j in range(len(strs)):
			if shortest[i] != strs[j][i]:
				return p
		p += shortest[i]
	return p
