''' FUNCTION TO ADD AN EDGE USING ADJACENCY LIST REPRESENTATION '''

# WEIGHTED GRAPH..


graph={}

def add_node(v):
    if v in graph:
        print(f"{v} is already present in the graph..")

    else:
        graph[v]=[]


# add edegs  to connect the node..

def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(f"{v1} is not present in the graph..")
    elif v2 not in graph:
        print(f"{v2} is not present in the graph..")
    else:
        list1=[v2,cost]
        list2=[v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)

add_node("A")
add_node("B")
add_node("C")


add_edge("A","B",10)
add_edge("A","C",5)

print(graph)

