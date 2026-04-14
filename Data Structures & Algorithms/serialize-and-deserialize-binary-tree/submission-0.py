# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # bfs -> mark no node as "N"
    # [1,2,3,null,null,4,5] -> [1, 2, 3, "N", "N", 4, 5]

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        res = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "N":
            return None
        root = TreeNode(int(vals[0]))
        q = deque()
        q.append(root)
        curr = 1 
        while q:
            node = q.popleft()
            if vals[curr] != "N":
                node.left = TreeNode(int(vals[curr]))
                q.append(node.left)
            curr += 1 
            if vals[curr] != "N":
                node.right = TreeNode(int(vals[curr]))
                q.append(node.right)
            curr += 1

        return root
