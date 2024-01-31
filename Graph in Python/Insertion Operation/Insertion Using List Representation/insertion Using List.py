''' FUNCTION TO ADD A NODE USING ADJACENCY LIST REPRESENTATION '''
graph={}

def add_node(v):
    if v in graph:
        print(f"{v} is already present in the graph..")

    else:
        graph[v]=[]     # key is V and the value is Empty...

add_node("F")
add_node("B")
print(graph)