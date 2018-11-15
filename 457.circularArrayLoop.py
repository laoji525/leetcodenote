class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) == 1:
            return False
        n = len(nums)
        for i in range(n):
			if type(nums[i]) != int:
				continue
			if nums[i] % n == 0:
				continue
			d = nums[i] > 0
			mark = str(i)
			while type(nums[i]) == int and d ^ (nums[i] < 0) and nums[i]% n != 0:
				step = nums[i]
				nums[i] = mark
				i = (i + step) % n
			if nums[i] == mark:
				return True
		return False
