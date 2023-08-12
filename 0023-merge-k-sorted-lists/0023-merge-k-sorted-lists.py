# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                list1  = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                temp.append(self.merge(list1, list2))
            lists = temp
        return lists[0]

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
        if list2:
            curr.next = list2
        return dummy.next

"""
LINKED LIST
- have already gone through 2 solutions
    - first was doing the same method as merging 2 lists, but having pointers for each list
    - second was merging first and second, then that result and third, and so on and so forth
    - this method will be merging pairs of lists, and storing that, then merging the new pairs

- Overall idea is to merge pairs of lists until all the lists are merged
- To do this have a temporary lists that stores the current state of the merged lists
- So pretty much merge pairs and add result to temp list
- then after each pair is merged, set lists = temp
- repeat until lists only has end result (1 final merged list)
"""