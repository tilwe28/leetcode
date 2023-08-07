# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

"""

how to reverse direction of two elements in linked list:
[1, 2] -> [2, 1]
head = {val: 1, next: {val: 2, next: None}}
temp = head.next
head.next = None
                    temp = {val: 2, next: None} [1]
temp.next = head
head = temp
                    temp = {val:2, next: {val: 1, next: None}} [2, 1]


"""