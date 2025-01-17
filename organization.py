# let's make a chart representating the chart of an orgranization

class TreeNode():
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.parent = None
        self.childnodes = []

    def add_child(self,child_node):
        self.childnodes.append(child_node)
        child_node.parent = self

    def get_level(self):
        level = 0
        p=self.parent
        while p:
            p = p.parent
            level+=1
        return level

    def print_tree(self,value=None):
        prefix = 3*self.get_level() * " " + "*-"

        if value == "name":
            print(f"{prefix} {self.name}", end="\n\n")
            for child in self.childnodes:
                child.print_tree(value)

        elif value == "designation":
            print(f"{prefix} {self.designation}", end="\n\n")
            for child in self.childnodes:
                child.print_tree(value)

        else:
            print(f"{prefix} {self.name} {self.designation}", end="\n\n")
            for child in self.childnodes:
                child.print_tree(value)


def build_tree():
    root = TreeNode("Nirajan", "(CEO)")

    cto_node = TreeNode("Nisha", "(CTO)")
    hr_node = TreeNode("Niruta", "(HR Manager)")
    ir_node = TreeNode("Jamuna", "(IR Manager)")
    apm_node = TreeNode("Raju", "(Application Manager)")
    rct_node = TreeNode("Khagaraj", "(Recruit Manager)")
    pm_node = TreeNode("Samrat", "(Policy Manager)")
    cd_node = TreeNode("Prakash", "(Cloud Manager)")
    ap_node = TreeNode("Anup", "(Application Manager)")

    cto_node.add_child(ir_node)
    cto_node.add_child(apm_node)

    hr_node.add_child(rct_node)
    hr_node.add_child(pm_node)

    ir_node.add_child(cd_node)
    ir_node.add_child(ap_node)

    root.add_child(cto_node)
    root.add_child(hr_node)

    return root

if __name__=="__main__":
    org_tree = build_tree()
    org_tree.print_tree()
    org_tree.print_tree("name")
    org_tree.print_tree("designation")