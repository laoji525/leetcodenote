class BSTIterator:

  def __init__(self, root):
    self.stack = []
    self.push(root)
    
  def hasNext(self):
    return self.stack
    
  def next(self):
    tempNode = self.stack.pop()
    self.push(tempNode.right)
    return tempNode.val
    
  def push(self, node):
    while node:
      self.stack.append(node)
      node = node.left
