# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val 
#         self.left = left < val
#         self.right = right > val
from collections import deque
class Solution:
    def recurse(self, node, min_val, max_val):
        if not node:
            return True
        if min_val != None and node.val <= min_val:
            return False
        if max_val != None and node.val >= max_val:
            return False
        return self.recurse(node.right, node.val, max_val) and self.recurse(node.left, min_val, node.val)
    

    def isValidBST(self, root: TreeNode | None) -> bool:
        
        # while left is good we need a max and min value ->
        # if val > left and val < right < parent if from right
        return self.recurse(root.left, None, root.val) and self.recurse(root.right, root.val, None)