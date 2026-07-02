"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # If node is None => return []
        # Else make a copy of the node and then DFS to attach the neighbors to that node
        if not node:
            return None
        migrated_nodes = {} # Dict of value to Node
        def dfs(node):
            if node in migrated_nodes:
                return migrated_nodes[node]
            clone = Node(node.val)
            migrated_nodes[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone
        dfs(node)
        print("Migrated Nodes: ", migrated_nodes[node])
        return migrated_nodes[node]