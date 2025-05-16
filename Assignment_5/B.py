import sys
sys.setrecursionlimit(2*100000+5)

def getChildrenNodes(matrix, node_idx):
    return matrix[node_idx - 1][0]

def getColor(matrix, node_idx):
    color_code = matrix[node_idx - 1][1]
    if color_code == 0: return 'white'
    elif color_code == 1: return 'grey'
    elif color_code == 2: return 'black'

def color(matrix, node_idx, color):
    if color == 'white':
        matrix[node_idx - 1][1] = 0
    elif color == 'grey':
        matrix[node_idx - 1][1] = 1
    elif color == 'black':
        matrix[node_idx - 1][1] = 2

res = []

def dfs(mat, src):
    res.append(str(src))
    color(mat, src, 'grey')
    for child in getChildrenNodes(mat, src):
        if getColor(mat, child) == 'white':
            dfs(mat, child)
    
    color(mat, src, 'black')
    


n, m = list(map(int, input().split()))
mat = []
for i in range(n):
    mat.append([[]])
for node in mat:
    node.append(0)

ul = list(map(int, input().split()))
vl = list(map(int, input().split()))

for i in range(m):
    u = ul[i]
    v = vl[i]
    mat[u - 1][0].append(v)
    mat[v - 1][0].append(u)


dfs(mat,1)
print(' '.join(res))