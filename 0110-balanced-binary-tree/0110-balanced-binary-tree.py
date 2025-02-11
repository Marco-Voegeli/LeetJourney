# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def getDepth(curr, agg_func):
            if curr:
                l_depth, l_balanced = getDepth(curr.left, agg_func)
                r_depth, r_balanced = getDepth(curr.right, agg_func)
                return 1 + agg_func(l_depth, r_depth), abs(l_depth - r_depth) <= 1 and l_balanced and r_balanced
            else:
                return 0, True
        if not root:
            return True
        depth, balanced = getDepth(root, max)
        return balanced
        