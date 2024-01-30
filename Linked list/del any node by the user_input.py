
# Del any node by the given user input value.


class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Linked_List:
    def __init__(self):
        self.head=None
    
    def print_linkedlist(self):
        if self.head is None:
            print("Linked list is empty..")

        else:
            n=self.head
            while n is not None:
                print(n.data)

                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node


    def del_by_value(self,x):
        if self.head is None:
            print("linked list is empty..")
            return
        if x==self.head.data:
            self.head=self.head.ref
            return
        
        n=self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("Node is not present..")
        else:
            n.ref=n.ref.ref

ll1=Linked_List()
ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_begin(30)
ll1.del_by_value(30)
ll1.print_linkedlist()
