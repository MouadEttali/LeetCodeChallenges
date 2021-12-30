class TreeNode:
  def __init__(self,data):
    self.data = data
    self.children = []
    self.parent = None

  def add_child(self,child):
    child.parent = self
    self.children.append(child)

  def get_level(self):
    level = 0
    p = self.parent
    while p:
      level += 1 
      p = p.parent
    return level

  def print_tree(self):
    spaces = ' ' * self.get_level() * 2
    prefix = spaces + '|__' if self.parent else ''
    print(prefix + self.data)
    for i in self.children:
      i.print_tree()


root = TreeNode("Electronics")
Laptops = TreeNode("Laptops")
TVS = TreeNode("TVS")
fridges = TreeNode("fridges")

Laptops.add_child(TreeNode("dell"))
Laptops.add_child(TreeNode("mac"))
Laptops.add_child(TreeNode("hp"))

TVS.add_child(TreeNode("lg"))
TVS.add_child(TreeNode("smart"))
TVS.add_child(TreeNode("samsung"))

fridges.add_child(TreeNode("lg"))
fridges.add_child(TreeNode("samsung"))


root.add_child(Laptops)
root.add_child(TVS)
root.add_child(fridges)
root.print_tree()
