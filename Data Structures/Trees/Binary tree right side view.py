"""Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it, return the
values of the nodes you can see ordered from top to bottom.

Example: Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        # Helper function to perform DFS and capture the rightmost element at each depth.
        def dfs(node, depth):
            if not node:
                return
            
            # If we are visiting this depth for the first time, add the node's value.
            if depth == len(result):
                result.append(node.val)
            
            # Visit the right subtree first, then the left subtree.
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        # Start DFS from the root.
        dfs(root, 0)
        
        return result
