# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        res = lists[0]
        for i in range(1, len(lists)):
            res = self.merge(res, lists[i])
        return res

    def merge(self, list1, list2):
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        return dummy.next
    
    # O(k * n) time

"""
LINKED LIST
- Previous method was to add minimum one at a time by checking all the currs of each list
- New method is merging each list while iterating through

- Already know how to merge 2 sorted lists
- Result will just be taking first list and merging it with second list, and repeating until
  there's only 1 list

- have result list and iterate through lists
- call merge function by doing res = merge(res, curr_list)
- return merge
"""