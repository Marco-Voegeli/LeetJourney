# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:

        def bfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [str(node.val)]
            queue = []
            base_path = str(node.val) + "->"
            left_ = bfs(node.left)
            right_ = bfs(node.right)
            if left_:
                for left in left_:
                    queue.append(base_path+str(left))
            if right_:
                for right in right_:
                    queue.append(base_path+str(right))
            return queue
        return bfs(root)


