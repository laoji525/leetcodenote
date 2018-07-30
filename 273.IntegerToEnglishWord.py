class Solution(object):
    def __init__(self):
        
        self.lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                      "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return 'Zero'
        res = ''
        n = 0
        if num >= 1000000000:
            n = num // 1000000000
            res = self.lessThan20[n] + ' Billion '
            num = num % 1000000000
        if num >= 1000000:
            res += self.help(num // 1000000)
            res += ' Million '
            num = num % 1000000
        if num >= 1000:
            res += self.help(num // 1000)
            res += ' Thousand '
            num = num % 1000
        res += self.help(num)
        if res[-1] == ' ':
            res = res[:len(res) - 1]
        return res

    def help(self, num):
        res = ''
        if num == 0:
            return ''

        if num < 20:
            res = self.lessThan20[num]
        elif num < 100:
            res = self.tens[num // 10] + ' '+ self.help(num % 10)
        else:
            res = self.lessThan20[num // 100] + " Hundred " + self.help(num % 100)
            
        if res[-1] == ' ':
            res = res[:len(res) - 1]
        return res
