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

    # Insert function
    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)

        return root

    # ---------------- Traversals ----------------

    # Preorder: Root -> Left -> Right
    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Inorder: Left -> Root -> Right
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    # Postorder: Left -> Right -> Root
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")


# ---------------- MAIN ----------------

bst = BST()

values = [15, 10, 20, 8, 12]

for val in values:
    bst.root = bst.insert(bst.root, val)

print("Preorder Traversal:")
bst.preorder(bst.root)

print("\nInorder Traversal:")
bst.inorder(bst.root)

print("\nPostorder Traversal:")
bst.postorder(bst.root)