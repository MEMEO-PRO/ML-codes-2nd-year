g = {}

print("Enter the nodes: ")
print("Enter -1 after entering the child nodes")
print("Enter -2 after entering the all nodes")

flag = 1
l = []

while flag:
    n = input(("Enter node: "))
    if n not in g and n!= "-2":
        g[n] = []
    elif n == "-2":
        break
    
    flag2 =1
    while flag2:
        print("Enter child nodes: ")
        cn = input("")
        if cn not in g[n] and cn != "-1" and cn != "-2":
            g[n].append(cn)
            g[cn] = []
        elif cn == "-1":
            flag2 = 0
        elif cn == "-2":
            flag2 = 0
            flag = 0
    
print(g)

v = []

def bfs(graph,start):
    q = []
    for node in graph[start]:
        q.append(node)
        # print(q)
        
    v.append(start)   
    print(start,end = " ")
    for node in q:
        print(node,end = " ")
        for i in graph[node]:
            q.append(i)
    return v
        
bfs(g,'a')
            
        

    
    



# print(bfs(g,'A'))