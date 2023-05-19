g = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F','G'],
    'D': ['H', 'I'],
    'E': ['J','K'],
    'F': [],
    'G': [],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}

def dfid(graph,start,goal,depth):
    for d in range(depth):
        v = []
        path = []
        if dfs(graph,start,goal,depth,v,path):
            return path
    return None

def dfs(graph,start,goal,depth,v,path):
    v.append(start)
    # print(start)
    path.append(start)
    
    if start == goal:
        return True
    if depth == 0:
        path.pop()
        return False
    
    for node in graph[start]:
        if node not in v:
            if dfs(graph, node,goal, depth-1, v, path):
                return True
            
    return False

result = dfid(g,'A', 'K', 4)
if result:
    print('Path found:', result)
else:
    print('No path found.')