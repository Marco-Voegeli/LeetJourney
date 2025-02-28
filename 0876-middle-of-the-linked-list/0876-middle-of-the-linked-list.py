# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Move the first pointer at half the speed of the second one
        p1 = head
        p2 = head
        while p2.next:
            p2 = p2.next
            p1 = p1.next
            if p2.next:
                p2 = p2.next
            
        return p1
            