# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # iteratively
        if not head:
            return None
        curr_node = head
        prev_node = None
        while curr_node:
            new_elem = ListNode(curr_node.val, prev_node)
            prev_node = new_elem
            curr_node = curr_node.next
        return new_elem

        # recursively
        def recurse(prev, curr):
            if not curr:
                return prev
            return recurse(ListNode(curr.val, prev), curr.next)
        return recurse(None, head)
        

