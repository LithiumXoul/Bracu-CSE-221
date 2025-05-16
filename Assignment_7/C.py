import heapq

def get_min_dangers(src, adj_l):
    n = len(adj_l) - 1 #Assumes 0 is a invalid node
    danger_l = [float('inf') for _ in range(n+1)]
    danger_l[src] = 0
    # visited = [0] * (n+1)
    heap = [(0, src)]

    while heap:
        cur_node_id = heapq.heappop(heap)[1]
        cur_node_danger = danger_l[cur_node_id]
        # visited[cur_node_id] = 1

        children = adj_l[cur_node_id]
        for child in children:
            child_node_id = child[0]
            child_node_weight = child[1]

            # if visited[child_node_id] == 1:
            #     continue

            if max(cur_node_danger, child_node_weight) < danger_l[child_node_id]:
                danger_l[child_node_id] = max(cur_node_danger, child_node_weight)
                heapq.heappush(heap, (danger_l[child_node_id], child_node_id))

    return danger_l


def main():
    n,m = list(map(int, input().split()))
    adj_l = [[] for _ in range(n + 1)]

    for i in range(m):
        u, v, w = list(map(int, input().split()))
        adj_l[u].append((v,w))
        adj_l[v].append((u,w))

    def mridu(elem):
        if elem == float('inf'):
            return '-1'
        
        return str(elem)

    res_l = get_min_dangers(1, adj_l)
    print(' '.join(list(map(mridu, res_l[1:]))))

main()

