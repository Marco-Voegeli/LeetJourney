# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameter_util(self, root)->int:
        if not root:
            return 0
        left_diam = self.diameter_util(root.left)
        right_diam = self.diameter_util(root.right)
        self.diameter = max(self.diameter, left_diam + right_diam)
        return 1 + max(left_diam, right_diam)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.diameter_util(root)
        return self.diameter
