import heapq

def get_min_distances(src, adj_l):
    n = len(adj_l) - 1 #Assumes 0 is a invalid node
    dist_l = [[float('inf'), float('inf')] for _ in range(n+1)]
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
