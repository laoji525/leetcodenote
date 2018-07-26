def wB(self, s, wordDict):
	list = [False] * (len(s) + 1)
	list[0] = True
	for i in range(1, len(s) + 1):
		for j in range( i - 1, -1, -1):
			if list[j] and s[j:i] in wordDict:
				list[i] = True
				break
	return list[-1]
