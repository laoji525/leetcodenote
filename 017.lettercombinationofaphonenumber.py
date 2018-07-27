def lCB(self, digits):
	if not digits or '1' in digits or '0' in digits:
		return []
	map = {}
	res = [[]]
	for d in digits:
		temp = []
		for r in res:
			for letter in map[d]:
				temp.append(r + [l])
		res = temp
	return ['',join(result) result for result in res]
