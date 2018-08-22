def rS(self, s):
	left, right = 0, len(s) - 1
	ls = list(s)
	while left < right:
		ls[left], ls[right] = ls[right], ls[left]
		left += 1
		right -= 1
	return ''.join(ls)
