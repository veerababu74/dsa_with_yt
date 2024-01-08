def add_node(v):
    global count
    if v in nodes:
        print("node is alredy here")
    else:
        count=count+1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp=[]
        for i in range(count):
            temp.append(0)
        graph.append(temp)

        
def add_edge_unorder(v1,v2):
    if v1 not in nodes:
        print(v1,"is not here")
    elif v2 not in nodes:
        print(v2,"is not here")

    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=1
        graph[index2][index1]=1

def add_edge_order(v1,v2):
    if v1 not in nodes:
        print(v1,"is not here")
    elif v2 not in nodes:
        print(v2,"is not here")

    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=1
        # graph[index2][index1]=1


def add_edge_unorder_with_weight(v1,v2,cost):
    if v1 not in nodes:
        print(v1,"is not here")
    elif v2 not in nodes:
        print(v2,"is not here")

    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=cost
        graph[index2][index1]=cost #remove this to its become orderd graph with edge


def print_graph():
    for i in range(count):
        for j in range(count):
            print(format(graph[i][j],">3"),end="")
        print()


nodes=[]
graph=[]
count=0

add_node("A")
add_node("c")
add_node("s")



print_graph()