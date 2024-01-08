def add_node(v):
    global nodes_cont
    if v in nodes:
        print(f"your entered node {v} is alredy exist")
    else:
        nodes_cont+=1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp=[]
        for i in  range(nodes_cont):
            temp.append(0)
        graph.append(temp)
def add_edge(v1,v2):
    if v1 not in nodes:
        print("v1 is not here")
    elif v2 not in nodes:
        print("v1 is not here")
        
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=1
        graph[index2][index2]=1 # comment this for directed graph

def add_edge_with_cost(v1,v2,cost):
    if v1 not in nodes:
        print("v1 is not here")
    elif v2 not in nodes:
        print("v1 is not here")
        
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=cost
        graph[index2][index2]=cost# comment this for directed graph
"""

| [    ]0    |
| [    ]1   |
| [    ]2   |
| [    ]3    |




"""
def delete_node(v):
    global nodes_cont
    if v not in nodes:
        print(v,"is not in nodes")
    else:
        index1=nodes.index(v)
        nodes_cont-=nodes_cont
        nodes.remove(v)
        graph.pop(index1)  #this for row
        for i in graph:
            i.pop(index1)

def delete_edege(v1,v2):
    if v1 not in nodes:
        print("nahi")
    elif v2 not in nodes:
        print("nahi")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=0
        graph[index2][index1]=0#comment this line to become a directed graph



def print_graph():
    for i in range(nodes_cont):
        for j in range(nodes_cont):
           print(format(graph[i][j],">3"),end="")
        print()

nodes_cont=0
nodes=[]
graph=[]

add_node("a")
add_node("b")
add_node("c")

print_graph()