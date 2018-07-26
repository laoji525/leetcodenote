def mR2(self, intervals):
	intervals.sort(key = lambda x: x.start)
	heap = []
	for i in intervals:
		if heap and i.start >= heap[0]:
			heapq.heapreplace(heap, i.end)
		else:
			heapq.heappush(heap, i.end)
	return len(heap)
