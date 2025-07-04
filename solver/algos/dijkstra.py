import heapq

def dijkstra(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = []
    heap = [(0, start, [])]  # (cost, position, path)

    min_cost = [[float('inf')]*cols for _ in range(rows)]
    min_cost[start[0]][start[1]] = 0

    while heap:
        cost, (x, y), path = heapq.heappop(heap)
        if (x, y) in visited:
            continue
        visited.append((x, y))
        path = path + [(x, y)]

        if (x, y) == end:
            return path, visited

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != 1:
                new_cost = cost + (maze[nx][ny] if maze[nx][ny] > 0 else 1)
                if new_cost < min_cost[nx][ny]:
                    min_cost[nx][ny] = new_cost
                    heapq.heappush(heap, (new_cost, (nx, ny), path))

    return [], visited
