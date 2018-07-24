def lCA(self, root, p, q):
  while root:
    if p.val < root.val > q.val:
      root = root.right
     elif: p.val > root.val < q.val:
      root = root.left
     else:
      return root
