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
    def append(self, node, parent):
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
        if node:
            self.printTree(node.left)
            print(node.value)
            self.printTree(node.right)

    def sortTree(self, list=[]):
        pass
    
    #organize tree with root=medianNode. left nodes < root & right nodes. right nodes > root & left nodes
    def optimizeTree(self, node=None):
        nodes = []
        leftnodes, rightnodes = []

        #nested function to turn BST into a list
        def makeTreeList(node, nodelist=[]):
            flag = False
            while node is not None:
                nodelist.append(node)
                if node.left is not None:
                    makeTreeList(node.left, nodelist)
                    if node.right is not None:
                        makeTreeList(node.right, nodelist)
            if node.left is None and node.right is None and flag == False:
                flag = True
                node = self.root.right
                makeTreeList(node, nodelist)
            return nodelist

        nodes = makeTreeList(node, nodes)

        #sort list and set root to midpoint
        nodes = self.sortTree(nodes)
        listlength = (len(nodes)-1)        
        midpoint = listlength/2

        #put nodes smaller than root into left list, put nodes greater than root into right list
        for i in range(0, midpoint):
            if i < midpoint:
                leftnodes.append(nodes[i])
        for q in range(midpoint+1, listlength):
            if q < listlength:
                rightnodes.append(nodes[q])

        #place sorted elements back into BST
        self.root = nodes[midpoint]
        self.root.right, self.root.left = None
        for m in range(len((leftnodes)-1), 0, -1):
            self.append(leftnodes[m])
        for n in range(0, len((rightnodes)-1)):
            self.append(rightnodes[n])


        
        

   

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