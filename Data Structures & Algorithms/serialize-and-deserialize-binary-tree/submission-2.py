# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        queue = deque()
        queue.append(root)
        serialized_tree = ""
        while queue:
            for length in range(len(queue)):
                node = queue.popleft()
                if node:
                    node_val_str = str(node.val)
                    serialized_tree+=node_val_str+","
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    serialized_tree+="null"+","
        return serialized_tree
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        dataList = data.split(",")
        if dataList[0] == "null":
            return None
        root = TreeNode(int(dataList[0]))
        queue = deque([root])
        index = 1
        while queue:
            parent = queue.popleft()    
            if dataList[index]!="null":
                parent.left = TreeNode(dataList[index])
                queue.append(parent.left)
            index+=1
            if dataList[index]!="null":
                parent.right = TreeNode(int(dataList[index]))
                queue.append(parent.right)
            index+=1
        
        return root


                
        
