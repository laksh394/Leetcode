"""There are two ways to traverse a tree non-recursively:

Breadth-first search (BFS):level order traversal
Depth-first search (DFS): inorder, preorder, postorder"""

""" BREADTH-FIRST SEARCH using queue """

from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to process each node (you can customize this function)
def process_node(node):
    print(node.data, end=' ')  # For example, just print the node's value

# BFS traversal function
def traverse_tree_bfs(root):
    if root is None:
        return
    q = deque()  # Use deque from collections for efficient queue operations
    q.append(root)
    while True:
        node_count = len(q)  # Get the number of nodes in the current layer
        if node_count == 0:
            break  # No more nodes to process

        # Process all nodes at the current level
        while node_count > 0:
            node = q.popleft()  # Pop the node from the front of the queue
            process_node(node)   # Process the current node (e.g., print it)

            # Add the children of the current node to the queue
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            node_count -= 1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Traverse the tree using BFS
traverse_tree_bfs(root)
