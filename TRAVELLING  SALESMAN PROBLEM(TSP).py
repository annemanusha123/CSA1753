from itertools import permutations

def tsp(graph, start=0):
    n = len(graph)
    nodes = list(range(n))
    nodes.remove(start)
    min_path, min_cost = None, float('inf')
    for p in permutations(nodes):
        cost = graph[start][p[0]] + sum(graph[p[i]][p[i+1]] for i in range(n-2)) + graph[p[-1]][start]
        if cost < min_cost:
            min_cost = cost
            min_path = (start,)+p+(start,)
    print("Path:", min_path)
    print("Cost:", min_cost)

# Example graph (distance matrix)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp(graph)
