def mA(self, height):
	left = 0
	right = len(height) - 1
	max_a = (right - left) * min(height[right], height[left])
	while left < right:
		if height[left] < height[right]:
			left += 1
		else:
			right -= 1
		max_a = max(max_a, (right - left) * min(height[right], height[left])
	return max_a
