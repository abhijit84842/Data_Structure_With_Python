# Search Operation..

class BST:
    def __init__(self,key):
        self.key=key            # for root
        self.lchild=None        # for left clild node
        self.rchild=None        # for right child node

    def insert(self,data):          # to insert the node or data

        if self.key is None:
            self.key=data
            return

        if self.key == data:            # to avoid the duplicate value..
            return

        if self.key > data:

            if self.lchild:     # if left child node is present
                self.lchild.insert(data)        # need to insert data recursively and compare the node

            else:               # if left child is not presecnt
                self.lchild= BST(data)


        else:                  # if given value is grater than of root node
            if self.rchild:             # if right child node is present
                self.rchild.insert(data)        # need to insert data recursively

            else:               # if right child is not presecnt
                self.rchild= BST(data)

    def search(self,data):              # method to search data from tree
        if self.key==data:          # if data is present in root node..
            print("Node is found..")
            return


        # compare with node..
        if self.key > data:
            if self.lchild:     # if left sub tree is present..
                self.lchild.search(data)        # search in left sub tree recursively
                print("node is present in left sub tree")
            else:
                print("Node is not present in left sub Tree..")
        else:
            if self.rchild:
                self.rchild.search(data)
                print("node is present in right sub tree")
            else:
                print("Node is not present in right sub Tree..")



root=BST(10)        # create object of BST class and this is the root node data

list1=[6,3,1,6,98,3,7]      # when we add the list of value in the node

for i in list1:
    root.insert(i)
root.search(5)






