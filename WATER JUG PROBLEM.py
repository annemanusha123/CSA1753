from collections import deque

def water_jug():
    visited = set()
    q = deque([(0, 0)])   # (jug4, jug3)

    while q:
        a, b = q.popleft()
        if a == 2:
            print("Reached:", (a, b))
            return

        for x, y in [(4,b),(a,3),(0,b),(a,0),
                     (min(4,a+b), max(0,a+b-4)),
                     (max(0,a+b-3), min(3,a+b))]:
            if (x, y) not in visited:
                visited.add((x, y))
                q.append((x, y))

water_jug()
