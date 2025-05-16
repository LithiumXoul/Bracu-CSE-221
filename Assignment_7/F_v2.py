import heapq

def get_min_and_2nd_min_distances(src, adj_l):
    n = len(adj_l) - 1 #assuming 0th node is invalid
    dist_l = [[float('inf'), float('inf')] for _ in range(n+1)] 
    dist_l[src][0] = 0

    pq = [(0, src)]
    while pq:
        cost_u, u = heapq.heappop(pq)
        for v, weight in adj_l[u]:
            cost_v = cost_u + weight
            # update shortest path
            if cost_v < dist_l[v][0]:
                dist_l[v][1] = dist_l[v][0]
                dist_l[v][0] = cost_v
                heapq.heappush(pq, (cost_v, v))
            # update second shortest path
            elif dist_l[v][0] < cost_v < dist_l[v][1]:
                dist_l[v][1] = cost_v
                heapq.heappush(pq, (cost_v, v))

    return dist_l

def main():
    n,m,s,d = list(map(int,input().split()))

    # Build adjacency list here
    adj_l = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = list(map(int, input().split()))
        adj_l[u].append((v, w))
        adj_l[v].append((u, w))


    res = get_min_and_2nd_min_distances(s, adj_l)[d][1]
    if res == float('inf'):
        print(-1)
        return
    print(res)

main()
