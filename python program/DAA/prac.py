# Node class
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# BST class
class BST:
    def __init__(self):
        self.root = None

    # ---------------- INSERT ----------------
    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)

        return root

    # ---------------- DELETE ----------------
    def delete(self, root, key):
        if root is None:
            return root

        # Step 1: Find the node
        if key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            # Case 1: No child
            if root.left is None and root.right is None:
                return None

            # Case 2: One child
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: Two children
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        return root

    # Find minimum value node
    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # ---------------- TRAVERSAL ----------------
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)


# ---------------- MAIN ----------------
bst = BST()

# Insert elements
values = [50, 30, 70, 20, 40, 60, 80]

for val in values:
    bst.root = bst.insert(bst.root, val)

print("Inorder Traversal after insertion:")
bst.inorder(bst.root)

# Delete a node
bst.root = bst.delete(bst.root, 30)

print("\nInorder Traversal after deleting 30:")
bst.inorder(bst.root)