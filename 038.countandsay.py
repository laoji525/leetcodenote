def countandsay(self,n):
  s = ''
  for _ in range(n-1):
    a = s[0]
    temp = ''
    count = 0
    for c in s:
      if c == a:
        count += 1
       else:
        temp = temp + str(count) + a
        a = c
        count = 1
      temp = temp + str(count) + a
      s = temp
   return s
