# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:

        # recursively
        def recurse(prev, curr):
            if not curr:
                return prev
            return recurse(ListNode(curr.val, prev), curr.next)
        return recurse(None, head)
        

