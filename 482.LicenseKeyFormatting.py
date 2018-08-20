def lKF(self, S, K):
	g = []
	temp = S.upper().replace('-', '')[::-1]
	for i in range(0, len(S), K):
		c = temp[i: i + K]
		if c == '': break
		g.append(c)
	return '-'.join(g)[::-1]
