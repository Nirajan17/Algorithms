# creating a tree for electronic items

class TreeNode():

    def __init__(self, node_data):
        self.parent = None
        self.child_nodes = []
        self.data = node_data

    def add_child(self,node):
        node.parent = self
        self.child_nodes.append(node)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level

    def print_tree(self):
        prefix = self.get_level() * "  " + "|--"
        print(prefix + self.data)
        for child in self.child_nodes:
            if self.child_nodes != 0:
                child.print_tree()

            

def build_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    Mobile = TreeNode("Mobiles")

    laptop.add_child(TreeNode("MacBook"))
    laptop.add_child(TreeNode("Chromebook"))
    laptop.add_child(TreeNode("Asus"))

    Mobile.add_child(TreeNode("Vivo"))
    Mobile.add_child(TreeNode("Apple"))
    Mobile.add_child(TreeNode("Huawei"))

    root.add_child(laptop)
    root.add_child(Mobile)

    return root

if __name__=='__main__':
    tree = build_tree()
    tree.print_tree()


        