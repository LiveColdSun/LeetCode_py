# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        left, right, i = head, head, 0
        while i < n and right.next is not None:
            right = right.next
            i += 1
        while right.next is not None:
            right = right.next
            left = left.next
        if left.next is not None:
            temp = left.next
            left.next = temp.next
        return left

if __name__ == "__main__":
    sol = Solution()
    l = ListNode(1)
    l.next  = ListNode(2)
    l.next
