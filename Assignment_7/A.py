from sys import exit

class Min_Queue:
    def __init__(self):
        self.l = []

    def push(self, node_id, priority):
        self.l.append([node_id, priority])

    def pop(self):
        min_idx = None
        for i in range(len(self.l)):
            if min_idx == None or self.l[min_idx][1] > self.l[i][1]:
                min_idx = i
        
        res = self.l.pop(min_idx)
        return res
    
    def set_priority(self, node_id, priority):
        for i in range(len(self.l)):
            if self.l[i][0] == node_id:
                self.l[i][1] = priority
                break

    def get_priority(self, node_id):
        for i in range(len(self.l)):
            if self.l[i][0] == node_id:
                return self.l[i][1]

    def get_queue(self):
        return self.l
    
    def is_empty(self):
        if len(self.l) == 0: return True
        return False
    
    def contains(self, node_id):
        for i in range(len(self.l)):
            if self.l[i][0] == node_id:
                return True
        return False


class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        # self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1
    def parent(self, pos):
        return pos//2
    def leftChild(self, pos):
        return 2 * pos
    def rightChild(self, pos):
        return (2 * pos) + 1
    def isLeaf(self, pos):
        return pos*2 > self.size
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]
    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if (self.Heap[pos][1] > self.Heap[self.leftChild(pos)][1] or
            self.Heap[pos][1] > self.Heap[self.rightChild(pos)][1]):
                if self.Heap[self.leftChild(pos)][1] < self.Heap[self.rightChild(pos)][1]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))
    def insert(self, element):
        if self.size >= self.maxsize :
            return
        self.size+= 1
        self.Heap[self.size] = element
        current = self.size
        while self.Heap[current][1] < self.Heap[self.parent(current)][1]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
    def Print(self):
        for i in range(1, (self.size//2)+1):
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1]))
    def minHeap(self):
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)
    def remove(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size-= 1
        self.minHeapify(self.FRONT)
        return popped




n,m,s,d = list(map(int, input().split()))
u_l = list(map(int, input().split()))
v_l = list(map(int, input().split()))
w_l = list(map(int, input().split()))

parent_l = [None for _ in range(n+1)]
res_l = [None for _ in range(n+1)]
adj_l = [[] for _ in range(n + 1)]
for i in range(m):
    u = u_l[i]
    v = v_l[i]
    w = w_l[i]

    adj_l[u].append((v,w))

min_q = Min_Queue()
for i in range(1, n+1):
    min_q.push(i, float('inf'))


min_q.set_priority(s, 0)

while not(min_q.is_empty()):
    cur_node_id, cur_node_priority = min_q.pop()
    res_l[cur_node_id] = cur_node_priority

    children = adj_l[cur_node_id]
    for child in children:

        child_node_id = child[0]
        child_edge_w = child[1]

        if not(min_q.contains(child_node_id)):
            continue

        # print(child_node_id)
        # print()
        # print(min_q.get_priority(child_node_id))

        if cur_node_priority + child_edge_w < min_q.get_priority(child_node_id):    
            min_q.set_priority(child_node_id, cur_node_priority + child_edge_w)
            parent_l[child_node_id] = cur_node_id

# print(res_l)
# print(parent_l)

if res_l[d] == float('inf'):
    print(-1)
    exit()

print(res_l[d])

path_list = []
cur_n = d
while cur_n != None:
    path_list.append(str(cur_n))
    cur_n = parent_l[cur_n]

path_list.reverse()
print(' '.join(path_list))
    