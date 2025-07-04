def dfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False]*cols for _ in range(rows)]
    parent = {}
    visited_order = []

    def dfs_recursive(x, y):
        # Check bounds and wall
        if not (0 <= x < rows and 0 <= y < cols):
            return False
        if visited[x][y] or maze[x][y] != 0:
            return False

        visited[x][y] = True
        visited_order.append((x, y))

        if (x, y) == end:
            return True

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if dfs_recursive(nx, ny):
                parent[(nx, ny)] = (x, y)
                return True

        return False

    dfs_recursive(start[0], start[1])

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
