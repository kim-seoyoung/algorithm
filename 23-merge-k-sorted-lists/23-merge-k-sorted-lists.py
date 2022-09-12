# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        output = ListNode()
        len_ = len(lists)
        q = []
        curr_lists = lists.copy()
        for i in range(len_):
            while curr_lists[i] is not None:
                heappush(q, curr_lists[i].val)
                curr_lists[i] = curr_lists[i].next
        
        curr_out = output
        while len(q) > 0:
            value = heappop(q)
            curr_out.next = ListNode(val=value)
            curr_out = curr_out.next
                
        output = output.next
            
        return output