def hammingD(self, x, y):
  return bin(x^y)[2:].count('1')
