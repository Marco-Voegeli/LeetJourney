# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # iteratively
        
        '''
        node = head
        if not head:
            return None
        reverso = ListNode(node.val, None)
        while node.next:
            reverso = ListNode(node.next.val, reverso)
            node = node.next
        return reverso
        '''
        # recursively
        def recurso(res, next_n):
            if not next_n:
                return res
            res = ListNode(next_n.val, res)
            return recurso(res, next_n.next)
        if not head:
            return None
        root = ListNode(head.val, None)
        return recurso(root, head.next)
