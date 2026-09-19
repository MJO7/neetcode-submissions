# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # abs(dfs(root.left)-dfs(root.right))

        # isBalanced = True
        
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            return 1 + max(left,right)

        def preorder(root):
            if not root:
                return True
            # print (root.val)
            if abs(dfs(root.left)-dfs(root.right))>1:
                # isBalanced = False
                return False
            if not preorder(root.left):
                return False
            if not preorder(root.right) :
                return False
            return True
        return preorder(root)
        