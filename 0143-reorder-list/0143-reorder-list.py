# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        curr, prev = second, None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        second = prev

        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

"""
LINKED LIST
- break list into 1st half and 2nd half
- take 2nd half and reverse it
- merge 1st half and new 2nd half together

- to break into 2 halves, use slow and fast pointer to find midway point
- then use new pointer to store start of 2nd half (second = slow.next)
- and then break the link by doing slow.next = None

- reverse by switching directions of links:
    curr, prev = second, None
    while curr:
        temp = curr.next    # ensure rest of list doesn't get lost
        curr.next = prev    # reverses direction of link
        prev = curr         # incrementing prev
        curr = temp         # getting back rest of link (allows to continue reversal)
- at the end set second = prev since prev is now the start of the reversed list

- merge by adding alternatively and making sure there are pointers so nothing gets lost
- /* NOTE: if list is even, then halves are equal length, otherwise, 1st half can be one bigger */
    while second:
        tmp1, tmp2 = first.next, second.next
        # merge
        first.next = second     # breaks link from first and rest of list but adds second hald
        second.next = tmp1      # inserts the broken link after adding second half
        # ^ results in start of reversed second half being inserted between
        first, second = tmp1, tmp2
"""