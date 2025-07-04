# # solver/solver.py

# from collections import deque

# def bfs(maze, start, end):
#     rows, cols = len(maze), len(maze[0])
#     queue = deque([(*start, [])])
#     visited = set()

#     while queue:
#         r, c, path = queue.popleft()
#         if (r, c) == tuple(end):
#             return path + [(r, c)]

#         if (r, c) in visited:
#             continue
#         visited.add((r, c))

#         for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
#                 queue.append((nr, nc, path + [(r, c)]))

#     return []  # No path
