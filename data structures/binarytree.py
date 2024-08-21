class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

class BST:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None
    
    def getHeight(self):
        if not self.isEmpty():
            return self._getHeight(self.root)
        else:
            return -1
        
    def _getHeight(self,current):
        height = 0
        if current.left:
            height += 1
            self._getHeight(current.left)
        #elif current.left is None:
        if current.right:
            height += 1
            self._getHeight(current.right)
        return height
    
    def getNumberOfNodes(self):
        return self._getNumberOfNodes(self.root)
    
    def _getNumberOfNodes(self,current):
        if current is None:
            return 0
        else:
            return self._getNumberOfNodes(current.left) + self._getNumberOfNodes(current.right) + 1

    def getRootData(self):
        return self.root

    def setRootData(self,rootnode):
        if not isinstance(rootnode,Node):
            rootnode = Node(rootnode)
        self.root = rootnode

    def add(self,node):
        if not isinstance(node,Node):
            node = Node(node)
        if self.root is None:
            self.setRootData(node)
        else:
            self._add(self.root,node)

    def _add(self,current,node):
        if node.value < current.value:
            if current.left is None:
                current.left = node
            else:
                self._add(current.left,node)
        else:
            if current.right is None:
                current.right = node
            else:
                self._add(current.right,node)

    def clear(self):
        self.root.value = None
        self.root.left = None
        self.root.right = None

    def getEntry(self, anEntry):
        return self._getEntry(self.root, anEntry)

    def _getEntry(self, current, anEntry):
        if current is None:
            return None
        elif anEntry == current.value:
            return current.value
        elif anEntry < current.value:
            return self._getEntry(current.left, anEntry)
        else:
            return self._getEntry(current.right, anEntry)

    def contains(self,data):
        return self._contains(self.root, data)
    
    def _contains(self,current,data):
        if current is None:
            return "Value not found in the BST"
        if current.value == data:
            return current.value
        elif data < current.value:
            return self._contains(current.left,data)
        else:
            return self._contains(current.right,data)
        
    def preorderTraverse(self): # root left right
        self._preorderTraverse(self.root)

    def _preorderTraverse(self,current):
        if current:
            print(current.value)
            self._preorderTraverse(current.left)
            self._preorderTraverse(current.right)

    def inorderTraverse(self): # left root right
        self._inorderTraverse(self.root)
    
    def _inorderTraverse(self,current):
        if current:
            self._inorderTraverse(current.left)
            print(current.value)
            self._inorderTraverse(current.right)
    
myBST = BST()

myBST.add(100)
myBST.add(50)
myBST.add(40)
myBST.add(150)
myBST.add(170)
myBST.add(120)

print(myBST.getHeight())