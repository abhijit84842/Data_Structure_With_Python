class BST:
    def __init__(self,key):
        self.key=key            # for root
        self.lchild=None        # for left clild node
        self.rchild=None        # for right child node

    def insert_data(self,data):          # to insert the node or data

        if self.key is None:
            self.key=data
            return

        if self.key == data:            # to avoid the duplicate value..
            return

        if self.key > data:

            if self.lchild:     # if left child node is present
                self.lchild.insert_data(data)        # need to insert data recursively and compare the node

            else:               # if left child is not presecnt
                self.lchild= BST(data)


        else:                  # if given value is grater than of root node
            if self.rchild:             # if right child node is present
                self.rchild.insert_data(data)        # need to insert data recursively

            else:               # if right child is not presecnt
                self.rchild= BST(data)


root=BST(10)        # create object and root is now 10  of BST class

list1=[20,2,50,40,10,26,30,35]      # when we add the list of value in the node

for i in list1:
    root.insert_data(i)






