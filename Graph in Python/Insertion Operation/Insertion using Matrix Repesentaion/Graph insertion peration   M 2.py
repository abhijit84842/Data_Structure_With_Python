''' FUNCTION TO ADD AN EDGE USING ADJACENCY MATRIX REPRESENTATION '''

# FOR UNDIRECTED OR UNWEIGHTED GRAPH




nodes=[]
graph=[]
''' node_count is the global variable'''
node_count=0        # how many node present in the grap

def add_node(v):
    global node_count  # to indicate the global variable..
    if v in nodes:
        print(f"{v} is already persent in graph")
    else:
        node_count=node_count + 1   # when adding the node number of node count increment by 1
        nodes.append(v)                # to add the node.

        for n in graph:         # we need to creat columm in the graph
            n.append(0) 


# here we create a seperated row

        temp=[]     # take a new list to add the rows

        for i in range(node_count):
            temp.append(0)
# after creating the row...we need to append row in the graph
        graph.append(temp)      # add in graph


''' Function to connect the edges with the node '''

def add_edge(v1,v2): # edge wiil connect with the nodes
    if v1 not in nodes:
        print(f"{v1} is not present in the nodes")
    elif v2 not in nodes:
        print(f"{v2} is not present in the nodes")
    
    else:
        index1=nodes.index(v1)  # find the index of the node
        index2=nodes.index(v2)      # find the index of the node
        graph[index1][index2]=1
        graph[index2][index1]=1     #  graph[A][B]=1   // graph[index of A][idex of B]=1
        



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

add_edge("A" , "B")         # connect the edge A - B

add_edge("A" , "C")         # connect the edge A - C

print('After adding the node...')
print(nodes)
print(graph)

print_graph()               # call the function



