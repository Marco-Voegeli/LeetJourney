# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diff = 0
        def getDepth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0, 0
            else:
                d_l, max_dl = getDepth(root.left)
                d_r, max_dr = getDepth(root.right)
                max_d = max(max_dl, max_dr)
                if d_l + d_r > max_d:
                    max_d = d_l + d_r
                depth = max(1 + d_l, 1 + d_r)
                return depth, max_d
        depth, max_d = getDepth(root)
        return max_d
