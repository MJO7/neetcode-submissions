# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, leftBoundary, rightBoundary):
            if not node:
                return True
            if node.val<=leftBoundary or node.val>=rightBoundary:
                return False
            return isValid(node.left,leftBoundary,node.val) and isValid(node.right,node.val,rightBoundary)
        return isValid(root,float("-inf"), float("inf"))