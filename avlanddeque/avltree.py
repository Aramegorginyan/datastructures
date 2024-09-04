class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1 

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self._insert(root.left, value)
        else:
            root.right = self._insert(root.right, value)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)


        if balance > 1 and value < root.left.value:
            return self.rotateRight(root)

        if balance < -1 and value > root.right.value:
            return self.rotateLeft(root)

        if balance > 1 and value > root.left.value:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        if balance < -1 and value < root.right.value:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, root, value):
        if not root:
            return root
        elif value < root.value:
            root.left = self._delete(root.left, value)
        elif value > root.value:
            root.right = self._delete(root.right, value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)

            root.value = temp.value
            root.right = self._delete(root.right, temp.value)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rotateRight(root)

        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.rotateLeft(root)

        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, root, value):
        if root is None or root.value == value:
            return root
        if value < root.value:
            return self._search(root.left, value)
        return self._search(root.right, value)

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rotateLeft(self, z):
        y = z.right
        tmp = y.left

        y.left = z
        z.right = tmp

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rotateRight(self, z):
        y = z.left
        tmp = y.right

        y.right = z
        z.left = tmp

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def inOrderTraversal(self):
        self._inOrderTraversal(self.root)
        print()

    def _inOrderTraversal(self, root):
        if root:
            self._inOrderTraversal(root.left)
            print(root.value, end=" ")
            self._inOrderTraversal(root.right)

avltree = AVLTree()