def iddfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited_order = []
    parent = {}

    def dls(x, y, depth, visited):
        if depth < 0:
            return False
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
            if not (0 <= nx < rows and 0 <= ny < cols):
                continue
            if not visited[nx][ny] and maze[nx][ny] == 0:
                parent[(nx, ny)] = (x, y)
                if dls(nx, ny, depth - 1, visited):
                    return True

        return False

    max_depth = rows * cols
    for depth in range(max_depth):
        visited = [[False]*cols for _ in range(rows)]
        if dls(start[0], start[1], depth, visited):
            break

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
