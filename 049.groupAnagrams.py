def gA(self, strs):
  r = collections.defaultdict(list)
  for s in strs:
    count = [0] * 26
    for c in s:
      count[ord(c) - ord('a')] += 1
    r[tuple(count)].append(s)
  return r.values()
