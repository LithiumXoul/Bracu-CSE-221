import heapq

def get_min_distances(src, adj_l):
    n = len(adj_l) - 1 #Assumes 0 is a invalid node
    dist_l = [float('inf') for _ in range(n+1)]
    dist_l[src] = 0
    visited = [0] * (n+1)
    parity_l = [None for _ in range(n+1)] #0, 1 are parities
    heap = [(0, src)]
    # parity_l[src] = 0

    while heap:
        cur_node_id = heapq.heappop(heap)[1]
        cur_node_dist = dist_l[cur_node_id]
        cur_node_parity = parity_l[cur_node_id]
        visited[cur_node_id] = 1

        children = adj_l[cur_node_id]
        for child in children:
            child_node_id = child[0]
            child_node_weight = child[1]
            child_node_parity = None
            if child_node_weight % 2 == 0: child_node_parity = 0
            else: child_node_parity = 1

            if visited[child_node_id] == 1:
                continue

            if cur_node_dist + child_node_weight < dist_l[child_node_id]:
                if cur_node_parity == None or cur_node_parity != child_node_parity:
                    dist_l[child_node_id] = cur_node_dist + child_node_weight
                    heapq.heappush(heap, (dist_l[child_node_id], child_node_id))
                    parity_l[child_node_id] = child_node_parity

    return dist_l


def main():
    n,m = list(map(int, input().split()))
    u_l = list(map(int, input().split()))
    v_l = list(map(int, input().split()))
    w_l = list(map(int, input().split()))
    adj_l = [[] for _ in range(n + 1)]
    for i in range(m):
        u = u_l[i]
        v = v_l[i]
        w = w_l[i]

        adj_l[u].append((v,w))

    res = get_min_distances(1, adj_l)[n]
    if res == float('inf'):
        print(-1)
        return
    print(res)

main()