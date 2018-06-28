class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = []
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                temp.append(nums[i])
        return temp
            
