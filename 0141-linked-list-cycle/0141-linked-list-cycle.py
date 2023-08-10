# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        slow, fast = head, head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

        # O(n) time
        # O(1) space

"""
LINKED LIST
- use slow and fast pointer
- if slow == fast, then cycle exists and should return True
- else, iteration finishes and should return False
"""