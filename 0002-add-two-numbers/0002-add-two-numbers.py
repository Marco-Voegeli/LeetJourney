# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addition(l1_next, l2_next, final_list, carry_on):
            if not l1_next and not l2_next: # L1 and L2 has no next
                if carry_on:
                    final_list.next = ListNode(carry_on)
                return final_list
            elif not l1_next:
                new_val = l2_next.val
                new_l1_next = None
                new_l2_next = l2_next.next
            elif not l2_next:
                new_val = l1_next.val
                new_l2_next = None
                new_l1_next = l1_next.next
            else:
                new_val = l1_next.val + l2_next.val
                new_l1_next = l1_next.next
                new_l2_next = l2_next.next
            new_val += carry_on
            next_list = ListNode(new_val%10) 
            carry_on = new_val//10
            next_list = addition(new_l1_next, new_l2_next, next_list, carry_on)
            final_list.next = next_list
            return final_list
        new_val = l1.val + l2.val
        carry_on = new_val//10 
        lRes = ListNode(new_val%10) 
        # First elements
        lRes = addition(l1.next, l2.next, lRes, carry_on)
        return lRes
        lRes = addition(l1.next, l2.next, lRes, carry_on)
        return lRes
        lRes = addition(l1.next, l2.next, lRes, carry_on)
        return lRes
            