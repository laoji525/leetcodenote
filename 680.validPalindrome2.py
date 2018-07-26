def vP(self, s):
	if s == s[::-1]:
		return True
	for i in range(len(s) // 2):
		if s[i] != s[~i]:
			del_b = s[i:~i]
			del_f = s[i+1: len(s)-i]
			if del_b == del_b[::-1] or del_f == del_f[::-1]:
				return True
			else:
				return False
