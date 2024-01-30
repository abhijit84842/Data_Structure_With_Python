'''Insert/add element at the end of linked list'''






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
            n=self.head
            while n is not None:
                print(n.data)

                n=n.ref     # to move the next node..
#''' ADD DATA BEGINING OF LINKED LIST '''
    def add_begin(self,data):
    
        new_node=Node(data)         # Create new node with the help of node class..
        new_node.ref=self.head      # Store new node ref of head refernce..
        self.head=new_node          # new node is the first node ..so we change the direction 

#''' ADD DATA THE END OF THE LINKED LIST '''

    def add_end(self,data):
        new_node=Node(data)
        
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node # reference will be store in new node..

ll1=linked_list()

ll1.add_begin(10)

ll1.add_begin(20)

ll1.add_begin(30)

ll1.add_end(100)

ll1.add_end(200)

print(ll1.print_LinkedList())


