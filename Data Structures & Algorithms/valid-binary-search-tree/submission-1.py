# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # recursively check that for each node:
        # left < node < right 
        # then if we go to the left child, itll be updated as 
        # left < node < parent node 
        # similarly if we go to the right child, itll be updated as 
        # parent node < node < right
        # use dfs, preorder traversal 

        def dfs(node, left, right):
            if not node:
                return True 
            
            if not (left < node.val < right):
                return False
            
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        
        return dfs(root, float("-inf"), float("inf"))