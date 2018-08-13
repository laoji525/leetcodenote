def aTN(self, l1, l2):
	res = prev = ListNode(Node)
	carry = 0
	while carry or l1 or l2:
		if l1:
			carry += l1.val
			l1 = l1.next
		if l2:
			carry += l2.val
			l2 = l2.next
		prev.next = ListNode(carry % 10)
		prev = prev.next
		carry //= 10
	return res.next
