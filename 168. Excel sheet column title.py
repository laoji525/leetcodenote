def convertToTitle(self, n):
  r = ''
  while n > 0:
    n -= 1
    r = chr(n%26+ord('A')) + r
    n /= 26
   return r
