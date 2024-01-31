class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None


root=BST(10)
print(root.key)     # output=10
print(root.lchild)  # output=None
print(root.rchild)  # output=None
