n = int(input())
adj_l = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = list(map(int, input().split()))
    adj_l[u-1].append(v-1)
    adj_l[v-1].append(u-1)

from collections import deque
def find_farthest_node(src, adl_l):

    global max_dist
    global max_dist_node
    max_dist = 0
    max_dist_node = src

    def bfs():

        global max_dist
        global max_dist_node

        visited = [0] * len(adj_l)
        dist = [-1] * len(adj_l)
        q = deque()
        q.append(src)
        visited[src] = 1
        dist[src] = 0

        while q:
            node = q.popleft()

            for neighbor in adj_l[node]:
                if visited[neighbor] == 1:
                    continue

                q.append(neighbor)
                visited[neighbor] = 1
                dist[neighbor] = dist[node] + 1
                if dist[neighbor] > max_dist:
                    max_dist = dist[neighbor]
                    max_dist_node = neighbor

    bfs()
    return max_dist_node, max_dist

f, _ = find_farthest_node(0, adj_l)
g, _dist = find_farthest_node(f, adj_l)

print(_dist)
print(f+1, g+1)

                