from collections import deque

def bfs(g, s):
    q, v = deque([s]), {s}
    while q:
        n = q.popleft()
        print(n, end=" ")
        for i in g[n]:
            if i not in v:
                v.add(i)
                q.append(i)

# Input graph
graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}

bfs(graph, 'A')
