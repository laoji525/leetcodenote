class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        s = s.strip(' ')
        temp = s.split(' ')[-1]


        return len(temp)
