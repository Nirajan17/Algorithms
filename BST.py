# implementing Binary Search Tree

class BinarySearchTree():
    def __init__(self,node_value):
        self.node_value = node_value
        self.left_node = None
        self.right_node = None

    def add_child(self,data):
        if self.node_value == data:
            # print(f"{data} already exits!")
            return
        
        if self.node_value > data:
            if self.left_node:
                self.left_node.add_child(data)
            else:
                self.left_node = BinarySearchTree(data)

        else:
            if self.right_node:
                self.right_node.add_child(data)
            else:
                self.right_node = BinarySearchTree(data)

    
    def inorder_traverse(self):
        elements = []
        # visiting the left subtree
        if self.left_node:
            elements += (self.left_node.inorder_traverse()) # use += to concatenate two lists, if used .apppend(), every a list will be appended which is not intended!

        # visiting the root node
        elements.append(self.node_value)  

        # visiting the right subtree
        if self.right_node:
            elements += (self.right_node.inorder_traverse())

        return elements

    def preorder_traverse(self):
        elements = []

        # visiting the root node
        elements.append(self.node_value)

        if self.left_node:
            elements += self.left_node.preorder_traverse()

        if self.right_node:
            elements += self.right_node.preorder_traverse()

        return elements

    def postorder_traverse(self):
        elements = []

        if self.left_node:
            elements += self.left_node.postorder_traverse()

        if self.right_node:
            elements += self.right_node.postorder_traverse()

        elements.append(self.node_value)
        return elements

def build_tree(values):
    root_node = BinarySearchTree(values[0])

    for i in range(1,len(values)):
        root_node.add_child(values[i])

    return root_node

if __name__=="__main__":
    numbers = [1,34,76,2,34,90,34,2,4,8,9,450]

    root_node = build_tree(numbers)

    print(f"\nInorder Traversal \n{root_node.inorder_traverse()}\n")
    print(f"Preorder Traversal \n{root_node.preorder_traverse()}\n")
    print(f"Postorder Traversal \n{root_node.postorder_traverse()}\n")

