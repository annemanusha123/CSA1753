from collections import deque

# State: (M_left, C_left, Boat)
# Boat: 0 = left side, 1 = right side

def is_valid(m, c):
    return (m == 0 or m >= c) and (3-m == 0 or 3-m >= 3-c)

def missionaries_cannibals():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        (m, c, b), path = queue.popleft()

        if (m, c, b) == goal:
            return path + [(m, c, b)]

        if (m, c, b) in visited:
            continue
        visited.add((m, c, b))

        for dm, dc in [(1,0),(0,1),(1,1),(2,0),(0,2)]:
            if b == 0:   # boat on left
                nm, nc = m-dm, c-dc
            else:        # boat on right
                nm, nc = m+dm, c+dc

            if 0 <= nm <= 3 and 0 <= nc <= 3 and is_valid(nm, nc):
                queue.append(((nm, nc, 1-b), path + [(m, c, b)]))

solution = missionaries_cannibals()

for state in solution:
    print(state)
