# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = []
        def preorder(root_node, greatest_value_so_far):
            if not root_node:
                return
            if root_node.val>=greatest_value_so_far:
                greatest_value_so_far = root_node.val
                res.append(root_node.val)

            preorder(root_node.left, greatest_value_so_far)
            preorder(root_node.right,greatest_value_so_far)

        preorder(root,float("-inf"))
        return len(res)