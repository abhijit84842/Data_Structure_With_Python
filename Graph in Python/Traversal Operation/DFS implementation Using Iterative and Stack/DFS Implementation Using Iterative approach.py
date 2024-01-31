

# UN-WEIGHTED GRAPH AND UN-DIRECTED GRAPH..

''' Implementation DFS using Iterative Approach.. '''


graph={}

#visited=set()

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
        #list1=[v2,cost]
        #list2=[v1,cost]
        graph[v1].append(v2)
        graph[v2].append(v1)


"""

''' DFS Traversal Operation..'''

def DFS(node,visited,graph):
    if node not in graph:
        print(f"{node} is not present in graph..")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)  # Recursion because we again call the DFS function..

"""   

''' DFS Using Iterative and Stack Approach.. '''

def DFSiterative(node,graph):
    visited_node = set()
    if node not in graph:
        print(f"{node} is not present in the graph..")
        return


    stack=[]        # where we push and pop node in stack..
    stack.append(node)    

    while stack:
        pop_node = stack.pop()      # pop the last node of in stack
        if pop_node not in visited_node:
            print(pop_node)
            visited_node.add(pop_node)
                    # need to finde the node of adjancey..
            for i in graph[pop_node]:
                stack.append(i)
    





add_node("A")
add_node("B")
add_node("C")


add_edge("A","B")
add_edge("A","C")

#DFS("B",visited,graph)     # DSF of Recursive Approach..

DFSiterative("B",graph)





