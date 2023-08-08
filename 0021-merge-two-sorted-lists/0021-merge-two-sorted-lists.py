# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        head, prev = None, None
        curr1, curr2 = list1, list2
        if curr1.val <= curr2.val:
            head = curr1
            curr1 = curr1.next
        else:
            head = curr2
            curr2 = curr2.next
        prev = head
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                prev.next = curr1
                curr1 = curr1.next
            else:
                prev.next = curr2
                curr2 = curr2.next
            prev = prev.next
        if curr1:
            prev.next = curr1
        elif curr2:
            prev.next = curr2
        return head

"""
LINKED LIST
~ have head node
~ iterate through each element of both linked lists (simultaneously)
~ add smallest node value
~ return head

~ to add smallest node value, compare curr1 and curr2 , then add to prev.next & increment corresponding curr
"""