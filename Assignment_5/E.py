from collections import deque

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

nodes_list = [None]

def contains_cycle(src = 1):
    q = deque()
    src_n = getNode(src)
    q.append(src)
    src_n.color = 1

    while q:
        a = q.popleft()
        a_n = getNode(a)

        for child in a_n.children:
            if getNode(child).color == 1:
                return True
            
            q.append(child)
            getNode(child).color = 1

        a_n.color = 2

    return False


n, m  = list(map(int, input().split()))
for i in range(1, n + 1):
    nodes_list.append(Node(i))

for _ in range(m):
    u, v = list(map(int, input().split()))
    getNode(u).children.append(v)

if contains_cycle(): print('YES')
else: print('NO')