# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # max -> ensure that the current node, is >= max -> it is a good node 
        # check children
        def dfs(root: TreeNode, maxVal) -> int:
            if not root:
                return 0 
            if root.val >= maxVal:
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
            else:
                return 0 + dfs(root.left, maxVal) + dfs(root.right, maxVal)
        
        return dfs(root, root.val)
