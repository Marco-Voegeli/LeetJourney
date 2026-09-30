# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sub_levelOrder(self, level, node: TreeNode | None):
        if None:
            return
        if level in self.level_dict:
            self.level_dict[level].append(node.val)
        else:
            self.level_dict[level] = [node.val]
        if node.left:
            self.sub_levelOrder(level + 1, node.left)
        if node.right: 
            self.sub_levelOrder(level + 1, node.right)
    
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        self.level_dict = {}


        self.sub_levelOrder(0, root)
        res = []
        for entry in self.level_dict:
            res.append(self.level_dict[entry])
        return res