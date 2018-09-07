def rNFE(self, head, n):
	dummy = ListNode(0)
	dummy.next = head
	first = second = dummy
	while n >= 0:
		first = first.next
		n -= 1
	while first:
		first = first.next
		second = second.next
	second.next = second.next.next
	return dummy.next
