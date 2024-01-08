def add_node(v):
    if v in graph:
        print(v,'is alredy exist')
    else:
        graph[v]=[]


def add_edge_unorder(v1,v2):
    if v1  not in graph:
        print(v1,"is not in graph")
    elif v2 not in graph:
        print(v2,"not in graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)


def add_edge_order(v1,v2):
    if v1  not in graph:
        print(v1,"is not in graph")
    elif v2 not in graph:
        print(v2,"not in graph")
    else:
        graph[v1].append(v2)

def add_edge_unorder_with_weight(v1,v2,cost):
    if v1  not in graph:
        print(v1,"is not in graph")
    elif v2 not in graph:
        print(v2,"not in graph")
    else:
        list1=[v1,cost]
        list2=[v2,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)  #remove this its become the order graph with weight



graph={}

add_node('a')
add_node('b')
add_node('c')
add_node('d')
add_edge_unorder_with_weight('a','c',10)
add_edge_unorder_with_weight('a','b',100)
add_edge_unorder_with_weight('b','d',2000)

print(graph)
