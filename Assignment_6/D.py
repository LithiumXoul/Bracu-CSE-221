n, r = list(map(int, input().split()))
adj_l = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = list(map(int, input().split()))
    adj_l[u-1].append(v-1)
    adj_l[v-1].append(u-1)

import sys
sys.setrecursionlimit(10**6)

visited = [0] * n #0 unvisited, 1 visited
size_count = [0] * n

def get_branches(n):
    return adj_l[n]

def calc_size(root):
    visited[root] = 1
    
    all_branches_size = 0
    for branch in get_branches(root):
        if visited[branch] == 1:
            continue
        branch_size = calc_size(branch)
        all_branches_size += branch_size

    size_count[root] = 1 + all_branches_size
    return 1 + all_branches_size

calc_size(r-1)

q = int(input())
for _ in range(q):
    x = int(input())
    print(size_count[x-1])

