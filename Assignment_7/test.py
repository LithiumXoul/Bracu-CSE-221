import heapq

heap = [(1,8)]
heapq.heappush(heap, (3,3))
heapq.heappush(heap, (2,6))

cur_node_id = heapq.heappop(heap)[1]
print(cur_node_id)

cur_node_id = heapq.heappop(heap)[1]
print(cur_node_id)

cur_node_id = heapq.heappop(heap)[1]
print(cur_node_id)