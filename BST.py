# implementing Binary Search Tree

class BinarySearchTree():
    def __init__(self,node_value):
        self.node_value = node_value
        self.left_node = None
        self.right_node = None

    def add_child(self,data):
        if self.node_value == data:
            print("Value already exits!")
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
            elements += self.left_node.inorder_traverse()

        # visiting the root node
        elements.append(self.node_value)

        # visiting the right subtree
        if self.right_node:
            elements += self.right_node.inorder_traverse()

        return elements

    def preorder_traverse(self):
        pass

    def postorder_traverse(self):
        pass


if __name__=="__main__":
    root_node = BinarySearchTree(10)
    root_node.add_child(18)
    root_node.add_child(34)
    root_node.add_child(23)
    root_node.add_child(67)
    root_node.add_child(5)
    root_node.add_child(90)

    print(root_node.inorder_traverse())

