# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
    	re = ListNode(0)
    	cur = re
    	temp = 0
    	while not (l1 == None  and l2 ==None):
    		extra = temp
    		if l1 != None :
    			extra += l1.val
    			l1 = l1.next

    		if l2 != None :
    			extra += l2.val
    			l2 = l2.next

    		temp = extra/10
    		cur.next = ListNode(extra%10)
    		cur = cur.next
    	if temp != 0:
    		cur.next = ListNode(temp)

    	return re.next

# to check the solution
# if __name__ == "__main__":
# 	l1 = ListNode(5)
# 	l1.next = ListNode(4)
# 	l1.next.next = ListNode(4)
# 	l2 = ListNode(2)
# 	l2.next = ListNode(6)
# 	l2.next.next = ListNode(3)
# 	l2.next.next.next = ListNode(4)
# 	s = Solution()
# 	# r = ListNode(0)
# 	r = s.addTwoNumbers(l1, l2)
# 	while r != None:
# 		print r.val
# 		r = r.next
    		

