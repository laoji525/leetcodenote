def plusOne(self, digits):
	for i in range(len(digits)):
		if digits[~i] < 9:
			digits[~i] += 1
			return digits
		else:
			digits[~i] = 0
	return [1] + [0] * len(digits)

def plusOne(self, digits):
	return map(int, list(str(int(''.join(map(str, digits))) + 1)))
