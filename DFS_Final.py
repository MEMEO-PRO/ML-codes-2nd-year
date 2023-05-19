# g = {
#     'A': ['B', 'C', 'D'],
#     'B': ['E', 'F'],
#     'C': [],
#     'D': [],
#     'E': [],
#     'F': []
# }


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

def dfs(graph,start):
    v.append(start)
    print(start,end=" ")
    for node in graph[start]:
        if node not in v:
            dfs(graph,node)

dfs(g,'A')














# def dfs(v,x):
#     reach[v]=1
#     for i in range(n):
#         k=0
#         for j in range(2):
#             if (adj[i][j] and reach[i]==0):
#                 if(i==x):
#                     print("Goal reached")
#                     break
#                 else:
#                     print(v,"->",i)
#                     dfs(i,x)


# n=int(input("Enter the height of tree:"))
# adj=[]
# reach=[]
# print("Enter the adjacency matrix:")
# for i in range(n):
#     t=[]
#     f=1
#     for j in range(n):
#         if(f<=2):
#             print("Enter the nodes connected to",i)
#             e=int(input())
#             if(e==-1):
#                 break
#             else:
#                 t.append(e)
#                 f+=1    
#     adj.append(t) 
#     reach.append(0)   
# print("The adjacency matrix is:",adj)
# s=int(input("Enter the source node:"))
# g=int(input("Enter the goal node:"))
# dfs(s,g)
# c=0
# for i in range(n):
#     if(reach[i]==1):
#         c+=1