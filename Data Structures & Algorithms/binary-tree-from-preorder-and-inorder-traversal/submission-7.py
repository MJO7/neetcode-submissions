# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:  
        
        indexMap = {}
        for index in range(len(inorder)):
            indexMap[inorder[index]] = index 

        self.preorder_index = 0
        def helper(left,right):
            if left>right:
                return None
            root = TreeNode(preorder[self.preorder_index])
            self.preorder_index+=1
            mid = indexMap[root.val]

            root.left = helper(left,mid-1)
            root.right = helper(mid+1,right)

            return root
        return helper(0,len(inorder)-1)