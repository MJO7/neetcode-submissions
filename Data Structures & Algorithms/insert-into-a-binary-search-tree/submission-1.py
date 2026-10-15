# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        originalRoot = root
        def dfs(root):
            if val>root.val and root.right==None:
                root.right = TreeNode(val)
                return originalRoot
            elif val<root.val and root.left ==None:
                root.left = TreeNode(val)
                return originalRoot
            if val>root.val:
                return dfs(root.right)
            elif val<root.val:
                return dfs(root.left)
            return None
        return dfs(root)