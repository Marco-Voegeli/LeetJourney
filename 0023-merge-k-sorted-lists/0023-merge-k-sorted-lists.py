# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Create a heap from the first elements of each list
        # Take the first elem of the heap (min)
        # Add new elem head elem of the list into the heap
        # sort heap out
        if not lists:
            return None
        heap_list = [(ls.val, i, ls.next) for (i, ls) in enumerate(lists) if ls is not None]
        if not heap_list:
            return None
        heapq.heapify(heap_list)
        head = ListNode()
        if not heap_list:
            return ListNode()
        curr = head
        while heap_list:
            (next_val, i, next_next) = heapq.heappop(heap_list)
            curr.next = ListNode(next_val, None)
            curr = curr.next
            if next_next is not None:
                heapq.heappush(heap_list, (next_next.val, i, next_next.next))
        return head.next
            
            