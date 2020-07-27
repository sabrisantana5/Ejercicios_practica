class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)
    def print_tree(self,traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root)
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root)
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root)
        else:
            print("not supported")
            return False
    def preorder_print(self,start):
        # root ->left->right
        if start: #checks if None
            print(start.value)
            self.preorder_print(start.left)
            self.preorder_print(start.right)
    def inorder_print(self,start):
        #left -> root -> right
        if start: #checks if None
            self.inorder_print(start.left)
            print(start.value)
            self.inorder_print(start.right)
    def postorder_print(self,start):
        #left -> right -> root
        if start: #checks if None
            self.inorder_print(start.left)
            self.inorder_print(start.right)
            print(start.value)
 
'''      1
       /   \
      2     3
     / \   / \
    4   5 6   7
'''
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("preorden")
tree.print_tree("preorder") #arriba a abajoizq a der
print("inorden")
tree.print_tree("inorder") #izq a der
print("postorden")
tree.print_tree("postorder") #de abajo a arriba izq a derecha
#1-2-4-5-3-6-7- preorden
#4-2-5-1-6-3-7- inorden
#4-2-5-6-3-7-1- postorden
