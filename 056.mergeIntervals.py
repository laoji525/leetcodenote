class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0: return []
        intervals.sort(key = lambda x : x.start)
        res = []
        temp = [intervals[0].start, intervals[0].end]
        for i in range(1, len(intervals)):
            if intervals[i].start <= temp[1]:
                temp[1] = max(intervals[i].end, temp[1])
            else:
                res.append(temp)
                temp = [intervals[i].start, intervals[i].end]
        res.append(temp)
        return res
