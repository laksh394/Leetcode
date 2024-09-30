"""Binary Tree Level Order Traversal II
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. 
(i.e., from left to right, level by level from leaf to root).

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(node: Optional[TreeNode], level: int, result: list[int]):
            if not node:
                return
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            bfs(node.left, level+1, result)
            bfs(node.right, level+1, result)
        result = []
        bfs(root, 0, result)
        return result[::-1]
