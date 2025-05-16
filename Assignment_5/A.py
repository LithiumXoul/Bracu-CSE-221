# import sys,io,os
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# print = sys.stdout.write


import queue

def getChildrenNodes(matrix, node_idx):
    return matrix[node_idx - 1][0]

def is_discovered(matrix, node_idx):
    if matrix[node_idx - 1][1] == 1: return True
    return False

def discover(matrix, node_idx):
    matrix[node_idx - 1][1] = 1


def bfs(mat, src = 1):
    q = queue.Queue()
    q.put(src)
    discover(mat, src)
    
    res = []

    while (q.qsize() != 0):
        n = q.get()
        res.append(str(n))

        children = getChildrenNodes(mat, n)
        for child in children:
            if not is_discovered(mat, child):
                q.put(child)
                discover(mat, child)


    print(' '.join(res))


n, m = list(map(int, input().split()))
mat = []
for i in range(n):
    mat.append([[]])
for _ in range(m):
    u, v = list(map(int, input().split()))
    mat[u - 1][0].append(v)
    mat[v - 1][0].append(u)

for node in mat:
    node.append(0)

# print(mat)
bfs(mat)
