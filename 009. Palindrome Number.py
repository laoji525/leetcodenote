class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = cmp(x,0)
        r = int(`s*x`[::-1])
        if x == 0:
            return True
        
        return bool((x%10!=0)*(s>0)*(x==r))
