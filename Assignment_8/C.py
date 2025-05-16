import sys
sys.setrecursionlimit(1 << 25)

class Set_Manager:
    def __init__(self, total_nodes):
        self.parent_l = [i for i in range(total_nodes + 1)]
        self.size = [1] * (total_nodes+1)

    def get_rep(self,i):
        if self.parent_l[i] == i:
            return i
        self.parent_l[i] = self.get_rep(self.parent_l[i])
        return self.parent_l[i]
    
    def union(self, a, b):
        rep_a = self.get_rep(a)
        rep_b = self.get_rep(b)
        if rep_a == rep_b:
            return False
        if self.size[rep_a] < self.size[rep_b]:
            rep_a, rep_b = rep_b, rep_a
        self.parent_l[rep_b] = rep_a
        self.size[rep_a] += self.size[rep_b]
        return True
    
    def in_same_set(self, a, b):
        return self.get_rep(a) == self.get_rep(b)

n, m = map(int, input().split())
edge_list = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edge_list.append((w, u, v))

edge_list.sort()
sets = Set_Manager(n)
mst_cost = 0
mst_edges = []
mst_set = set()

for w, u, v in edge_list:
    if sets.union(u, v):
        mst_cost += w
        mst_edges.append((u, v, w))
        mst_set.add((min(u, v), max(u, v), w))

if len(mst_edges) != n - 1:
    print(-1)
    exit()

adj = [[] for _ in range(n+1)]
for u, v, w in mst_edges:
    adj[u].append((v, w))
    adj[v].append((u, w))

LOG = 16
parent = [[-1]*LOG for _ in range(n+1)]
max_edge = [[0]*LOG for _ in range(n+1)]
depth = [0]*(n+1)

def dfs(u, p):
    for v, w in adj[u]:
        if v == p:
            continue
        depth[v] = depth[u] + 1
        parent[v][0] = u
        max_edge[v][0] = w
        dfs(v, u)

dfs(1, -1)

for j in range(1, LOG):
    for i in range(1, n+1):
        if parent[i][j-1] != -1:
            parent[i][j] = parent[parent[i][j-1]][j-1]
            max_edge[i][j] = max(max_edge[i][j-1], max_edge[parent[i][j-1]][j-1])

def get_max_edge(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]
    max_w = 0

    for i in range(LOG-1, -1, -1):
        if diff & (1 << i):
            max_w = max(max_w, max_edge[u][i])
            u = parent[u][i]

    if u == v:
        return max_w

    for i in range(LOG-1, -1, -1):
        if parent[u][i] != -1 and parent[u][i] != parent[v][i]:
            max_w = max(max_w, max_edge[u][i], max_edge[v][i])
            u = parent[u][i]
            v = parent[v][i]

    return max(max_w, max_edge[u][0], max_edge[v][0])

second_best = float('inf')
for w, u, v in edge_list:
    if (min(u, v), max(u, v), w) in mst_set:
        continue
    max_w = get_max_edge(u, v)
    if w > max_w:
        second_best = min(second_best, mst_cost - max_w + w)

print(second_best if second_best != float('inf') else -1)
