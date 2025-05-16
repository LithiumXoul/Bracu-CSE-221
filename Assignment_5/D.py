import queue

class Node:
    def __init__(self, id):
        self.id = id
        self.parent = None
        self.color = 0
        self.children = []        




def getNode(id):
    if type(id) != int:
        return None
    return nodes_list[id]


def bfs(src, dst):
    q = queue.Queue()
    q.put(src)
    getNode(src).color = 1
    
    found = False

    while(q.qsize() != 0 and found == False):
        n = q.get()
        n_node = getNode(n)
        for child in n_node.children:

            if child == dst:
                getNode(child).parent = n
                found = True
                break

            if getNode(child).color == 0:
                q.put(child)
                getNode(child).color = 1
                getNode(child).parent = n

def get_path(src, dst):
    if src == dst:
        return [str(src)]
    graph  = nodes_list
    for i in range(1, len(graph)):
        node = nodes_list[i]
        node.parent = None
        node.color = 0

    bfs(src, dst)
    path = []
    cur_node = getNode(dst)

    if cur_node.parent == None:
        return -1


    while cur_node != None:
        path.append(str(cur_node.id))
        cur_node = getNode(cur_node.parent)
    path.reverse()
    return path

nodes_list = [None]


n, m, s, d, k = list(map(int, input().split()))
for i in range(1, n + 1):
    nodes_list.append(Node(i))

for _ in range(m):
    u, v = list(map(int, input().split()))
    getNode(u).children.append(v)



a = get_path(s, k)
b = get_path(k, d)

res = []

if a == -1 or b == -1:
    res = ['-1']
else:
    res = a + b[1:]

if res[0] != '-1': print(len(res) - 1)
print(' '.join(res))