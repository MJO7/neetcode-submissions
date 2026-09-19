# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 1. if root null return 0
        # 2. maintain res = 0 which is the diameter(max length)
        # 3. compare the lenghts of the two subtrees of a node and add 1 to it, and if that's biger than res than make res that max lenght

        self.res = 0

        # return height
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left+right)
            return 1+max(left,right)

        dfs(root)
        return self.res
