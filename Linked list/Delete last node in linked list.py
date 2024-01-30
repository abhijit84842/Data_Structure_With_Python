
# Delete the last node from linked list..

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Linked_List:
    def __init__(self):
        self.head=None
    
    def print_linkedlist(self):
        if self.head is None:
            print("linked list is empty..")

        else:
            n=self.head
            while n is not None:
                print(n.data)

                n=n.ref

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    ''' Delete the last node from linked list..'''

    def del_end(self):
        if self.head is None:
            print("Linked list is empty, We can't perform del operation..")
        
        else:
            n=self.head 
            while n.ref.ref is not None:
                n=n.ref  
            n.ref=None

ll1=Linked_List()
ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_begin(30)       # Output=> 30,20,10

ll1.del_end()   # Output=> 30,20


ll1.print_linkedlist()
