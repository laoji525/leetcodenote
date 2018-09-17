def numJewelsInStones(self, J, S):
	res = 0
	for s in S:
		if s in J:
			res += 1
	return res
