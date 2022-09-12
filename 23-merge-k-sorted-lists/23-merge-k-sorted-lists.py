# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        output = ListNode()
        len_ = len(lists)
        q = PriorityQueue()
        curr_lists = lists.copy()
        for i in range(len_):
            if curr_lists[i] is not None:
                q.put((curr_lists[i].val, i))
        
        curr_out = output
        while not q.empty():
            value, idx = q.get()
            curr_out.next = ListNode(val=value)
            curr_lists[idx] = curr_lists[idx].next
            curr_out = curr_out.next
            if curr_lists[idx] is not None:
                q.put((curr_lists[idx].val, idx))
                
        output = output.next
            
        return output