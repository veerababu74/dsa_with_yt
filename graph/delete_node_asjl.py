def add_node(v):
    if v in graph:
        print("element alrey here")
    else:
        graph[v]=[]

def add_edge(v1,v2):
    if v1 not in graph:
        print("nahi")
    elif v2 not in graph:
        print("nahi")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

def add_edge_with_cost(v1,v2,cost):
    if v1 not in graph:
        print("nahi")
    elif v2 not in graph:
        print("nahi")
    else:
        temp1=[v1,cost]
        temp2=[v2,cost]
        graph[v1].append(temp2)
        graph[v2].append(temp1)


def del_node(v):
    if v not in graph:
        print("nahi")
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            if v in list1:
                list1.remove(v)
def del_node_have_cost(v):
    if v not in graph:
        print("nahi")
    else:
        graph.pop(v)
        for  i in graph:
            list1=graph[i]
            for j in list1:
                if v ==j[0]:
                    list1.remove(j)
                    break

def delete_edege(v1,v2):
    if v1 not in graph:
        print("nahi")
    elif v1 not in graph:
        print("nahi")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)

def del_edge_have_cost(v1,v2,cost):
    if v1 not in graph:
        print("nahi")
    elif v1 not in graph:
        print("nahi")
    else:
        temp=[v1,cost]
        temp1=[v2,cost]
        if temp1 in graph[v1]:
            graph[v1].remove(temp1)
            graph[v2].remove(temp)

graph={}

add_node("a")
add_node("b")
add_node("c")
add_node("d")
add_edge("a","c")
add_edge("d","c")
add_edge("d","b")
del_node('c')
print(graph)
