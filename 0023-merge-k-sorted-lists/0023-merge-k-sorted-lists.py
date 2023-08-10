# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy, k = ListNode(), len(lists)
        res, currs, total_size = dummy, [None] * k, 0
        for i,head in enumerate(lists):
            currs[i], curr = head, head
            while curr:
                total_size += 1
                curr = curr.next

        for i in range(total_size):
            min_node, min_index = ListNode(float('inf'), None), -1
            for j in range(k):
                if currs[j] and currs[j].val < min_node.val:
                    min_node, min_index = currs[j], j
            res.next = min_node
            res = res.next
            currs[min_index] = currs[min_index].next
        return dummy.next

        # O(k^2 * n) time, where k is number of lists and n is amount of items in each list
        # O(k) space

"""
LINKED LIST
- set k = len(lists)
- have dummy node to start list (avoids edge cases)
- start iterating through lists (iterate through make length of sublist)
- check each curr and add minimum value to result
- iterate corresponding curr
- repeat until it reached the end of each list

- to iterate, have a list of k curr (currs = [] * k)
- then iterate through outer list
    - set currs[k] to head of kth list
    - also at same time, track number of total items

- iterate with for loop in range of total items (need to add that many items for end result)
- have inner loop that checks the curr value for the sublists
    - keep track of which list contains the minimum
- have min_node = currs[0] and min_index = 0, and override if currs[k].val < min_node.val
- once min is found, add to result with res.next = min_node
  and then increment with currs[min_index] = currs[min_index].next

- remember to check for null pointer exceptions (don't do checks if currs[k] doesn't exist)
    - only happens once everything in that sublist has already been added

return dummy.next
"""