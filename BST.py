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

    def search(self, val):
        if self.node_value == val:
            return True
        
        if val < self.node_value:
            if self.left_node:
                return self.left_node.search(val)
            else:
                return False
            
        if val > self.node_value:
            if self.right_node:
                return self.right_node.search(val)
            else:
                return False

    def find_min(self):
        if self.left_node == None:
            return self.node_value
        else:
            return self.left_node.find_min()
        
    def find_max(self):
        if self.right_node == None:
            return self.node_value
        else:
            return self.right_node.find_max()

    def calculate_sum(self):
        sum_left = self.left_node.calculate_sum() if self.left_node else 0
        sum_right = self.right_node.calculate_sum() if self.right_node else 0

        return sum_left+sum_right+self.node_value
    
    def delete_node(self, val):
        if val > self.node_value:
            if self.right_node:
                self.right_node = self.right_node.delete_node(val)
        elif val < self.node_value:
            if self.left_node:
                self.left_node = self.left_node.delete_node(val)
        
        else:
            # for node which don't have any children
            if self.left_node is None and self.right_node is None:
                return None
            # for node having one child
            if self.left_node is None:
                return self.right_node
            if self.right_node is None:
                return self.left_node
            
            min_value = self.right_node.find_min(self.right_node)
            self.node_value = min_value
            self.right_node = self.right_node.delete_node(min_value)

        return self

        

def build_tree(values):
    root_node = BinarySearchTree(values[0])

    for i in range(1,len(values)):
        root_node.add_child(values[i])

    return root_node

if __name__=="__main__":
    numbers = [10,34,76,20,34,90,34,200,2,49,85,933,450]

    root_node = build_tree(numbers)

    print(f"\nInorder Traversal \n{root_node.inorder_traverse()}\n")
    print(f"Preorder Traversal \n{root_node.preorder_traverse()}\n")
    print(f"Postorder Traversal \n{root_node.postorder_traverse()}\n")

    print(f"minimum value is {root_node.find_min()}")
    print(f"maximum value is {root_node.find_max()}")

    print(f"Sum of the tree is {root_node.calculate_sum()}")

    s1 = root_node.delete_node(200)
    print(f"\nInorder Traversal \n{s1.inorder_traverse()}\n")
