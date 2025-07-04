from collections import deque

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False]*cols for _ in range(rows)]
    parent = {}
    queue = deque([start])
    visited[start[0]][start[1]] = True

    visited_order = []  # <- for heatmap

    while queue:
        x, y = queue.popleft()
        visited_order.append((x, y))  # Log visited cell

        if (x, y) == end:
            break

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and maze[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = True
                parent[(nx, ny)] = (x, y)

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
