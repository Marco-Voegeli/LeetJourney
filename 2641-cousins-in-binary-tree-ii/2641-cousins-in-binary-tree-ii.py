# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recordSumRec(root, depth, depth_sum):
            left = root.left
            right = root.right
            if len(depth_sum) <= depth:
                depth_sum.append(root.val)
            else:
                depth_sum[depth] += root.val
            if left:
                depthSumL = recordSumRec(left, depth + 1, depth_sum)
                #depth_sum = [sum(x) for x in zip(depth_sum, depthSumL)]
                depth_sum = depthSumL
            if right:
                depthSumR = recordSumRec(right, depth + 1, depth_sum)
                depth_sum = depthSumR
            return depth_sum
        
        def update_node(root, depth, depth_sum):
            if depth == 0:
                root.val = depth_sum[depth] - root.val
            l = root.left
            r = root.right
            sum_childs = 0
            # Sum children
            if l:
                sum_childs += l.val
            if r:
                sum_childs += r.val
            # Update children
            if l:
                l.val = depth_sum[depth + 1] - sum_childs
                l = update_node(l, depth + 1, depth_sum)
            if r:
                r.val = depth_sum[depth + 1] - sum_childs
                r = update_node(r, depth + 1, depth_sum)
            return root
        depth_sum = []
        res = recordSumRec(root, 0, depth_sum)
        updated = update_node(root, 0, res)
        return updated