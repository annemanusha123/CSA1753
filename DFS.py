def dfs(g, s, visited=set()):
    print(s, end=" ")
    visited.add(s)
    for i in g[s]:
        if i not in visited:
            dfs(g, i, visited)

# Input graph
graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}

dfs(graph, 'A')
