''' DELETE NODE  OPERATION Using LIST REPREENTATION  '''

''' FUNCTION TO DELTETE A NODE  USING LIST  REPRESENTATION '''



# WEIGHTED AND UNDIRECTED GRAPH..Delete list repressentation..


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




''' DELETE NODE OPERATION USING LIST REPRESENTATION..'''

def del_node(v):
    if v not in graph:          # check v is present or not..
        print(f"{v} is not present in the graph..")

    else:
        graph.pop(v)        # del key of V and value from the graph..

        for i in graph:             # i is represent the key of dict..
            list1 = graph[i]                # value of every key is the list
            for j in list1:
                if v==j[0]:
                    list1.remove(j)
                    break






add_node("A")
add_node("B")
add_node("C")


add_edge("A","B",10)            # connect A - B
add_edge("A","C",5)           # Connect A - C

del_node("B")       # call del_node method to del B from  the list..

print(graph)






