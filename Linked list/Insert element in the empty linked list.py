'''Insert/add element in empty  linked list'''






class Node:             # Create the node with the help of node class
    def __init__(self,data):
        self.data=data
        self.ref=None

class linked_list:          # linked list class
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


    def insert_empty(self,data):

        if self.head is None:
            new_node=Node(data)

            self.head=new_node           # new node is the first node ..so we change the direction ...and head store the new_node ref..
        else:
            print("Linked list is not empty..")








ll1=linked_list()



ll1.insert_empty(10)  # when linked list is empty..

ll1.insert_empty(10)        # OUTPUT="Linked list is not empty.."

print(ll1.print_LinkedList())


