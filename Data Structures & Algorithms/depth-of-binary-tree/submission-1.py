# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # if root does not exist return 0
        # 1. if the left subtree has more maxdepth than right subtree return 1+maxdepth of left subtree
        # 2. or vice versa
        
        if not root:
            return 0
        if self.maxDepth(root.left)>self.maxDepth(root.right):
            return 1+self.maxDepth(root.left)
        else:
            return 1+self.maxDepth(root.right)