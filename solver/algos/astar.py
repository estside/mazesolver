import heapq

def astar(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False]*cols for _ in range(rows)]
    visited_order = []
    parent = {}

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

    heap = [(heuristic(start, end), 0, start)]  # (f_score, g_score, position)
    g_score = {start: 0}

    while heap:
        f, g, (x, y) = heapq.heappop(heap)
        if visited[x][y]:
            continue
        visited[x][y] = True
        visited_order.append((x, y))

        if (x, y) == end:
            break

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and maze[nx][ny] == 0:
                new_g = g + 1
                neighbor = (nx, ny)
                if neighbor not in g_score or new_g < g_score[neighbor]:
                    g_score[neighbor] = new_g
                    f_score = new_g + heuristic(neighbor, end)
                    heapq.heappush(heap, (f_score, new_g, neighbor))
                    parent[neighbor] = (x, y)

    # Reconstruct path
    path = []
    node = end
    while node in parent:
        path.append(node)
        node = parent[node]
    if path:
        path.append(start)
        path.reverse()

    return path, visited_order
