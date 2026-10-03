# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # iteratively
        prev = None
        node = head
        if not head:
            return None
        reverso = ListNode(node.val, None)
        while node.next:
            reverso = ListNode(node.next.val, reverso)
            node = node.next
        return reverso