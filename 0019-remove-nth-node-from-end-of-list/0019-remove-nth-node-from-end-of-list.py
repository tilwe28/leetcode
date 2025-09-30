# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        curr = head
        while curr:
            sz += 1
            curr = curr.next
        
        prev, curr = None, head
        for _ in range(sz - n):
            prev = curr
            curr = curr.next
        
        if sz == n:
            tmp = head.next
            head.next
            head = tmp
        else:
            prev.next = curr.next
        return head

"""
Generic case:
..., node_to_remove, ...
Edge cases:
1) node_to_remove, ...   # n == sz
..., node_to_remove      # n == 1
node_to_remove           # n == sz == 1
"""