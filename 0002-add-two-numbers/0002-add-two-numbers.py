# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = tail = ListNode()
        carry = 0

        while l1 or l2:
            curr_sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = curr_sum >= 10

            tmp = ListNode(curr_sum % 10)
            tail.next = tmp
            tail = tmp

            l1 = (l1.next if l1 else l1)
            l2 = (l2.next if l2 else l2)

        if carry:
            tmp = ListNode(1)
            tail.next = tmp
            tail = tmp

        return (head.next if head else head)


"""
O(n):
- maintain pointer to each list
- maintain carry
- while either has more digits, continue the sum
- maintain the sum as a linked list (keep appending to head)
"""