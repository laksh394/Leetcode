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
        d=defaultdict(int)
        def foo(x,depth):
            if x.left: foo(x.left,depth+1)
            d[depth]=x.val
            if x.right: foo(x.right,depth+1)
        if root: foo(root,0)
        return [d[i] for i in sorted(d.keys())]
