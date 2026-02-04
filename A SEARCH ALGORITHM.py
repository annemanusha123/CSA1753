import heapq

def astar(graph, start, goal, h):
    open_list = []
    heapq.heappush(open_list, (h[start], start))

    g = {start: 0}
    parent = {start: None}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor, cost in graph[current]:
            new_g = g[current] + cost
            if neighbor not in g or new_g < g[neighbor]:
                g[neighbor] = new_g
                f = new_g + h[neighbor]
                heapq.heappush(open_list, (f, neighbor))
                parent[neighbor] = current

    return None


# ----- Graph -----
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 4)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# ----- Heuristic values -----
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 1,
    'F': 0
}

# ----- Run A* -----
path = astar(graph, 'A', 'F', heuristic)
print("Optimal Path using A*:", path)
