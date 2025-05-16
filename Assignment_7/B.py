import heapq

def get_min_distances(src, adj_l):
    n = len(adj_l) - 1 #Assumes 0 is a invalid node
    dist_l = [float('inf') for _ in range(n+1)]
    dist_l[src] = 0
    visited = [0] * (n+1)
    heap = [(0, src)]

    while heap:
        cur_node_id = heapq.heappop(heap)[1]
        cur_node_dist = dist_l[cur_node_id]
        visited[cur_node_id] = 1

        children = adj_l[cur_node_id]
        for child in children:
            child_node_id = child[0]
            child_node_weight = child[1]

            if visited[child_node_id] == 1:
                continue

            if cur_node_dist + child_node_weight < dist_l[child_node_id]:
                dist_l[child_node_id] = cur_node_dist + child_node_weight
                heapq.heappush(heap, (dist_l[child_node_id], child_node_id))

    return dist_l



def main():
    n,m,s,t = list(map(int, input().split()))
    adj_l = [[] for _ in range(n + 1)]

    for i in range(m):
        u, v, w = list(map(int, input().split()))
        adj_l[u].append((v,w))
        
    a = get_min_distances(s, adj_l)
    b = get_min_distances(t, adj_l)

    res_node = None
    res_node_dist = None

    for i in range(len(a)):
        if a[i] == float('inf') or b[i] == float('inf'):
            continue

        if res_node_dist == None or res_node_dist > max(a[i], b[i]):
            res_node = i
            res_node_dist = max(a[i], b[i])

    if res_node_dist == None:
        print(-1)
        return
    
    print(f'{res_node_dist} {res_node}')

main()

    
