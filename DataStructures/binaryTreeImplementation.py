class BinaryTreeNode:
  def __init__(self,data):
    self.data = data
    self.right = None
    self.left = None

  def add_child(self,data):
    if self.data == data:
      return
    
    if data < self.data:
      if self.left:
        self.left.add_child(data)
      else:
        self.left = BinaryTreeNode(data)
    else:
      if self.right:
        self.right.add_child(data)
      else:
        self.right = BinaryTreeNode(data)

  def in_order_traversal(self):
    elements = []
    if self.left:
      elements += self.left.in_order_traversal()

    elements.append(self.data)

    if self.right:
      elements += self.right.in_order_traversal()
    return elements
    
  def search(self,val):

    if self.data == val:
      return True

    if self.data > val:
      if self.left:
        self.left.search(val)
      else:
        return False


    if self.data < val:
      if self.right:
        return self.right.search(val)
      else:
        return False
    

  def find_min(self):
    if self.left is None:
      return self.data
    return self.left.find_min()

  def find_max(self):
    if self.right is None:
      return self.data
    return self.right.find_max()


  def delete(self,val):
    if val < self.data:
      if self.left:
        self.left = self.left.delete(val)
    elif val > self.data:
      if self.right:
        self.right = self.right.delete(val)
    else:
      if self.left is None and self.right is None:
        return None
      if self.left is None:
        return self.right
      if self.right is None:
        return self.left

      min_val = self.right.find_min()
      self.data = min_val
      self.right = self.right.delete(min_val)
