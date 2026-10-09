"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloneMap = {}

        def clone(node):
            if node in cloneMap:
                return cloneMap[node]
            else:
                copy = Node(node.val)
                cloneMap[node] = copy
                for i in node.neighbors:
                    copy.neighbors.append(clone(i))

                return copy
        
        return clone(node)