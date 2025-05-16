import heapq

def get_min_distances(src, weight_l, adj_l):
    n = len(adj_l) - 1 #Assumes 0 is a invalid node
    dist_l = [float('inf') for _ in range(n+1)]
    dist_l[src] = weight_l[src]
    visited = [0] * (n+1)
    heap = [(weight_l[src], src)]

    while heap:
        cur_node_id = heapq.heappop(heap)[1]
        cur_node_dist = dist_l[cur_node_id]
        visited[cur_node_id] = 1

        children = adj_l[cur_node_id]
        for child in children:
            child_node_id = child
            child_node_weight = weight_l[child]

            if visited[child_node_id] == 1:
                continue

            if cur_node_dist + child_node_weight < dist_l[child_node_id]:
                dist_l[child_node_id] = cur_node_dist + child_node_weight
                heapq.heappush(heap, (dist_l[child_node_id], child_node_id))

    return dist_l

def main():
    n,m,s,d = list(map(int, input().split()))
    adj_l = [[] for _ in range(n + 1)]
    weight_l = list(map(int,input().split()))
    weight_l = [0] + weight_l

    for i in range(m):
        u, v = list(map(int, input().split()))
        adj_l[u].append(v)

    res = get_min_distances(s, weight_l, adj_l)
    if res[d] == float('inf'):
        print(-1)
        return
    print(res[d])

main()