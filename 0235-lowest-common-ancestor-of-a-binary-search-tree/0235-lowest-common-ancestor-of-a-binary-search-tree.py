# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def inbetween(curr_val, p, q):
            if curr_val <= p.val and curr_val >= q.val:
                return True
            if curr_val >= p.val and curr_val <= q.val:
                return True
            return False

        curr = root
        while(not inbetween(curr.val, p, q)):
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right

        return curr
        