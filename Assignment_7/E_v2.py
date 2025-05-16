import heapq

def get_min_distances(src, adj_l):
    n = len(adj_l) - 1  # Assumes 0 is an invalid node

    dist_l = [[float('inf')] * 2 for _ in range(n + 1)]  # dist[node][parity]
    visited = [[0] * 2 for _ in range(n + 1)]            # visited[node][parity]
    heap = []

    # Start with undefined parity (-1) so first edge can be either even or odd
    heapq.heappush(heap, (0, src, -1))

    while heap:
        cur_node = heapq.heappop(heap)
        cur_node_dist = cur_node[0]
        cur_node_id = cur_node[1]
        prev_parity = cur_node[2]

        children = adj_l[cur_node_id]
        for child in children:
            child_node_id = child[0]
            child_edge_w = child[1]
            child_parity = child_edge_w % 2

            if prev_parity == child_parity:
                continue  # must alternate parity

            if cur_node_dist + child_edge_w < dist_l[child_node_id][child_parity]:
                dist_l[child_node_id][child_parity] = cur_node_dist + child_edge_w
                heapq.heappush(heap, (dist_l[child_node_id][child_parity], child_node_id, child_parity))

    return dist_l


def main():
    n, m = list(map(int, input().split()))
    u_l = list(map(int, input().split()))
    v_l = list(map(int, input().split()))
    w_l = list(map(int, input().split()))
    adj_l = [[] for _ in range(n + 1)]
    for i in range(m):
        u = u_l[i]
        v = v_l[i]
        w = w_l[i]
        adj_l[u].append((v, w))

    res_l = get_min_distances(1, adj_l)
    res = min(res_l[n][0], res_l[n][1])
    if res == float('inf'):
        print(-1)
        return
    print(res)

main()
