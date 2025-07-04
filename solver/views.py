from django.shortcuts import render
from django.http import JsonResponse
# from .solver import bfs
import json

def index(request):
    return render(request, "index.html")


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .algos.bfs import bfs
from .algos.dfs import dfs
from .algos.iddfs import iddfs
from .algos.astar import astar
from .algos.dijkstra import dijkstra


@csrf_exempt
def solve(request):
    if request.method == "POST":
        data = json.loads(request.body)
        maze = data['maze']
        start = tuple(data['start'])
        end = tuple(data['end'])
        algo = data['algo']

        if maze[start[0]][start[1]] == 1 or maze[end[0]][end[1]] == 1:
            return JsonResponse({'path': []})

        if algo == 'bfs':
            path, visited = bfs(maze, start, end)
        elif algo == 'dfs':
            path, visited = dfs(maze, start, end)
        elif algo == 'iddfs':
            path, visited = iddfs(maze, start, end)
        elif algo == 'astar':
            path, visited = astar(maze, start, end)
        elif algo == 'dijkstra':
            path, visited = dijkstra(maze, start, end)

        
        else:
            path, visited = [], []

    
        return JsonResponse({'path': path, 'visited': visited, 'algo_used': algo})