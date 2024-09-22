# Definition for a binary tree node.
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Insert method to add new nodes to the tree
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    # Find the minimum value node in the right subtree (inorder successor)
    def minValueNode(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    # Delete method to remove a node from the tree
    def delete(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            # Case 1: Node to be deleted has no child (it's a leaf)
            if self.left is None and self.right is None:
                return None
            # Case 2: Node to be deleted has only one child
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            # Case 3: Node to be deleted has two children
            else:
                # Find the inorder successor (smallest in the right subtree)
                temp = self.right.minValueNode()
                self.data = temp.data
                # Delete the inorder successor
                self.right = self.right.delete(temp.data)
        return self

    # Method to print the tree in an in-order traversal
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

# Create the binary tree and insert nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(10)
root.insert(13)

print("Tree before deletion:")
root.PrintTree()

# Delete a node
root.delete(6)

print("\nTree after deleting 6:")
root.PrintTree()
