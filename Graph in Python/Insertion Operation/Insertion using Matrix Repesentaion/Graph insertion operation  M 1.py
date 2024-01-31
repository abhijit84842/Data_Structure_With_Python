''' FUNCTION TO ADD A NEW NODE USING ADJACENCY MATRIX REPRESENTATION '''

nodes=[]  # To store the all node
graph=[]  # To strore all the matrix or graph..
''' node_count is the global variable'''
node_count=0        # how many node present in the grap

def add_node(v):
    global node_count  # to indicate the global variable..
    if v in nodes:
        print(f"{v} is already persent in graph")
    else:
        node_count=node_count + 1   # when adding the node number of node count increment by 1
        nodes.append(v)                # to add the node.

        
# columm create..
        for n in graph:         # we need to creat columm in the graph
            n.append(0) 


# here we create a seperated row

        temp=[]     # take a new list to add the rows

        for i in range(node_count):
            temp.append(0)
# after creating the row...we need to append row in the graph
        graph.append(temp)      # add in graph

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph [i] [j] , end=" ")

        print()         # we use print function to see the list in different line..



print('Before adding the node..')
print(nodes)
print(graph)

add_node("A")

add_node("B")

add_node("C")

print('After adding the node...')
print(nodes)
print(graph)

print_graph()               # call the function










