# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find midpoint
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # merge
        l1, l2 = head, prev
        while l1 and l2:
            # add l2 to l1
            temp = l1.next
            l1.next = l2
            l1 = temp

            # add l1 to l2
            temp = l2.next
            l2.next = l1
            l2 = temp