'''Singly linked program using Traversal operation'''

class Node:             # Create the node..
    def __init__(self,data):
        self.data=data
        self.ref=None

class linked_list:
    def __init__(self):
        self.head=None          # create AN EMPTY linkedlist...

    def print_LinkedList(self):
        if self.head is None:
            print("Linked list is empty..")
        
        else:
            n=self.head     # here n also helps for moving from one node to another node..
            while n is not None:
                print(n.data)

                n=n.ref     # to move the next node..

ll1=linked_list()
print(ll1.print_LinkedList())



    
