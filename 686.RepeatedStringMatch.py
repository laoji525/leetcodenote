def repeatedStringMatch(self, A, B):
	if B in A:
		return 1
	if set(B) > set(A):
		return -1
	n = len(B) // len(A)
	if B in A * n:
		return n
	if B in A * (n + 1):
		return n + 1
	if B in A * (n + 2):
		return n + 2
