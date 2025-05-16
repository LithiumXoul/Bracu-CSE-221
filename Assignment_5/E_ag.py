import sys
sys.setrecursionlimit(10**6)

def has_cycle(n, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)

    visited = [0] * (n + 1)  

    def dfs(node):
        visited[node] = 1  
        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                if dfs(neighbor):
                    return True
            elif visited[neighbor] == 1:
                return True  
        visited[node] = 2  
        return False

    for i in range(1, n + 1):
        if visited[i] == 0:
            if dfs(i):
                return "YES"
    return "NO"

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

print(has_cycle(n, edges))

