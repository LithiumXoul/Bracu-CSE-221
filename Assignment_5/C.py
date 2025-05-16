import queue

class Node:
    def __init__(self, id):
        self.id = id
        self.parent = None
        self.color = 0
        self.children = []        

nodes_list = [None]

def getNode(id):
    if type(id) != int:
        return None
    return nodes_list[id]

n, m, s, d = list(map(int, input().split()))
for i in range(1, n + 1):
    nodes_list.append(Node(i))

ul = list(map(int, input().split()))
vl = list(map(int, input().split()))

for k in range(m):
    u = ul[k]
    v = vl[k]

    getNode(u).children.append(v)
    getNode(v).children.append(u)

for y in range(1, n+1):
    nodes_list[y].children.sort()


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
        
    
def main():
    if s == d:
        print(0)
        print(s)
        return
    
    res = []
    bfs(s,d)
    cur_node = getNode(d)

    if cur_node.parent == None:
        print(-1)
        return

    total_edge = -1
    while cur_node != None:
        res.append(str(cur_node.id))
        cur_node = getNode(cur_node.parent)
        total_edge += 1
    res.reverse()
    print(total_edge)
    print(' '.join(res))

main()