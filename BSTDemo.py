class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def printNode(self):
        return self.value
class BinaryTree():
    def __init__(self, root):
        self.root = root

    #traverse to leaf, add node to end
    def append(self, node, parent=None):
        if parent == None:
            parent = self.root

            #if node < parent, go left
        if node.value < parent.value:
            if parent.left:
                self.append(node, parent.left)
            else:
                parent.left = node
            #if node > parent, go right
        elif node.value > parent.value:
            if parent.right:
                self.append(node, parent.right)
            else:
                parent.right = node
        
    def printTree(self, node=None):
        if node == None:
            node = self.root
        print(node.printNode())
        if node.left:
            self.printTree(node.left)
        if node.right:
            self.printTree(node.right)

    def traverseTree(self, node=None):
        if node == None:
            node = self.root
        if node.left:
            self.traverseTree(node.left)
        if node.right:
            self.traverseTree(node.right)
        return node
    #organize tree with root=medianNode. left nodes < root & right nodes. right nodes > root & left nodes
    def optimizeTree(self):
        nodes, leftnodes, rightnodes = []

        #put all nodes into a list
        #sort list and set root to midpoint
        #put nodes smaller than root into left list, put nodes greater than root into right list



    def remove():
        pass

    def insert():
        pass

    def search(self):
        pass

    




root = Node(10)
tree = BinaryTree(root)
tree.append(Node(11))
tree.append(Node(9))
print(root.right.printNode())
#tree.printTree()