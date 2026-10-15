# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indexMap={}
        for i in range(len(inorder)):
            indexMap[inorder[i]] = i
        self.postorder_index = len(postorder)-1
        
        def helper(left,right):
            if (left>right):
                return None
            root = TreeNode(postorder[self.postorder_index])
            self.postorder_index-=1
            mid = indexMap[root.val]
            root.right = helper(mid+1,right)
            root.left = helper(left,mid-1)
            return root
        return helper(0,len(inorder)-1)

        