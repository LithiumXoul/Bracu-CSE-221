from sys import exit
import heapq

n,m,s,d = list(map(int, input().split()))
u_l = list(map(int, input().split()))
v_l = list(map(int, input().split()))
w_l = list(map(int, input().split()))

parent_l = [None for _ in range(n+1)]
dist_l = [float('inf') for _ in range(n+1)]
dist_l[s] = 0
adj_l = [[] for _ in range(n + 1)]
visited = [0] * (n+1)
for i in range(m):
    u = u_l[i]
    v = v_l[i]
    w = w_l[i]

    adj_l[u].append((v,w))

heap = [(0,s)]

while len(heap) > 0:
    cur_node_id = heapq.heappop(heap)[1]
    cur_node_priority = dist_l[cur_node_id]
    visited[cur_node_id] = 1

    children = adj_l[cur_node_id]

    for child in children:

        child_node_id = child[0]
        child_edge_w = child[1]

        if visited[child_node_id] == 1:
            continue 

        if cur_node_priority + child_edge_w < dist_l[child_node_id]:    
            dist_l[child_node_id] =  cur_node_priority + child_edge_w
            parent_l[child_node_id] = cur_node_id
            heapq.heappush(heap, (cur_node_priority + child_edge_w, child_node_id))



if dist_l[d] == float('inf'):
    print(-1)
    exit()

print(dist_l[d])

path_list = []
cur_n = d
while cur_n != None:
    path_list.append(str(cur_n))
    cur_n = parent_l[cur_n]

path_list.reverse()
print(' '.join(path_list))


    