# Definition for a binary tree node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Pre-order traversal(iterative)
def traverse_tree_preorder(root):
    if root is None:
        return
    
    stack = []
    stack.append(root)
    
    while stack:
        node = stack.pop()  # Pop the node from the stack
        print(node.data, end=' ')   # Do the actual work (e.g., print the node value)

        # Push right child first, then left, because stack is LIFO
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# In-order traversal (iterative)
def traverse_tree_inorder(root):
    stack = []
    node = root
    
    while node is not None or stack:
        # Reach the left-most node of the current node
        while node is not None:
            stack.append(node)
            node = node.left
        
        # Current node must be the left-most node
        node = stack.pop()
        print(node.data, end=' ')  # Do the actual work (e.g., print the node value)
        
        # We have visited the node and its left subtree, now go to the right subtree
        node = node.right


# Post-order traversal (iterative) 
def traverse_tree_postorder(root):
    if root is None:
        return
    
    stack1 = []
    stack2 = []
    
    stack1.append(root)
    
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        
        # Push left and right children to stack1
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    
    # Process all nodes in the second stack
    while stack2:
        node = stack2.pop()
        print(node.data, end=' ')  # Do the actual work (e.g., print the node value)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Traverse tree in Pre-order
traverse_tree_preorder(root)
# Traverse tree in In-order
traverse_tree_inorder(root)
# Traverse tree in Post-order
traverse_tree_postorder(root)
