class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self. parent = None
    def add_child(self,child):
        self.child = child 
        child.parent = self
        self.children.append(child)
    def get_level(self):
        level = 0 
        p = self.parent
        while p :
            p = p.parent
            level += 1
        return level 
    def print_tree(self):
        print('  '*self.get_level() + '|--', end = '')
        print(self.data)
        if self.children:
            for each in self.children:
                each.print_tree()

def run():
    #root = TreeNode('Eletronics')
    root = TreeNode('Swimming championships')
    
    # laptop = TreeNode('Laptop')
    # root.add_child(laptop)
    # laptop.add_child(TreeNode('Mac'))
    # laptop.add_child(TreeNode('Windows'))
    # laptop.add_child(TreeNode('Linux'))

    Tokyo_olympics = TreeNode('Tokyo_olympics')
    root.add_child(Tokyo_olympics)
    Tokyo_olympics.add_child(TreeNode('Mens 100m Breaststroke'))
    Tokyo_olympics.add_child(TreeNode('Mens 100m Butterfly'))
    Tokyo_olympics.add_child(TreeNode('Mens 100m Freestyle'))


    Fina = TreeNode('Fina')
    root.add_child(Fina)
    Fina.add_child(TreeNode('Mens 100m Breaststroke'))
    Fina.add_child(TreeNode('Mens 100m Butterfly'))
    Fina.add_child(TreeNode('Mens 100m Freestyle'))

    root.print_tree()

    #return root
if __name__ == '__main__':
    run()
    pass
