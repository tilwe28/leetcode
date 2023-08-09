# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        head = prev

        # remove
        prev, curr = None, head
        for i in range(n - 1):
            prev = curr
            curr = curr.next
        if prev:
            prev.next = curr.next
        else:
            head = curr.next

        # reverse
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
        
"""
LINKED LIST
- reverse list
- go forward n-1 times
- remove that node
- reverse again

- to remove node, keep track of prev and curr
    EXAMPLE: list = 1 -> 2 -> 3 -> 4 -> 5, n = 2    result = 1 -> 2 -> 3 -> 5
              rev = 5 -> 4 -> 3 -> 2 -> 1, n = 2

    prev, curr = None, head
    for i in range(n - 1):      # loops once in given example
        prev = curr
        curr = curr.next
                                # after loop prev = 5, curr = 4
    # to remove
    prev.next = curr.next

    EDGE CASE: list = 1 -> 2, n = 1     result = 1
                rev = 2 -> 1, n = 1
    
"""