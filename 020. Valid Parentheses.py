class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 == 1:
            return False
        dict = {"]":"[","}":"{",")":"("}
        stack = []
        for ch in s:
            if ch in dict.values():
                stack.append(ch)
            elif ch in dict.keys():
                a = dict[ch]
                if stack == []:
                    return False
                if a != stack.pop():
                    return False
        return stack == []
