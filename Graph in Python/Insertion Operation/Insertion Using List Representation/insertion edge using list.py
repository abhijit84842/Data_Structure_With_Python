''' FUNCTION TO ADD AN EDGE USING ADJACENCY LIST REPRESENTATION '''

# UNDIRECTED UNWEIGHTED GRAPh..


graph={}

def add_node(v):
    if v in graph:
        print(f"{v} is already present in the graph..")

    else:
        graph[v]=[]


# add edegs  to connect the node..

def add_edge(v1,v2):
    if v1 not in graph:
        print(f"{v1} is not present in the graph..")
    elif v2 not in graph:
        print(f"{v2} is not present in the graph..")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

add_node("A")
add_node("B")
add_node("C")


add_edge("A","B")
add_edge("A","C")

print(graph)

