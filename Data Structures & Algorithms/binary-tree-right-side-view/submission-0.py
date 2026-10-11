# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        res = []
        queue.append(root)

        while queue:
            queLen = len(queue)
            level_right_side_view = -1
            for i in range(queLen):
                node = queue.popleft()
                if node:
                    level_right_side_view = (node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level_right_side_view!=-1:
                res.append(level_right_side_view)
        
        return res