class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        if len(nums)==1 and nums[0]==0:
            return 1
        if nums[0]!=0:
            return 0
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return i+1
