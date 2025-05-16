n, m = list(map(int, input().split()))
mat = []
for i in range(n):
    mat.append([[]])
for _ in range(m):
    u, v = list(map(int, input().split()))
    mat[u - 1][0].append(v-1)
    mat[v - 1][0].append(u-1)

for node in mat:
    node.append(0)


from collections import deque


def main(mat):

    res = 0

    def is_red(src):
        if mat[src][1] == 2: return True
        return False
    def is_blue(src):
        if mat[src][1] == 3: return True
        return False
    def make_red(src):
        mat[src][1] = 2
    def make_blue(src):
        mat[src][1] = 3


    def get_neighbors(src):
        return mat[src][0]
    
    def bfs(src = 0):

        red = 0
        blue = 0

        q = deque()
        q.append(src)
        make_red(src)
        red += 1

        while not(len(q) == 0):
            cur_n_id = q.popleft()

            for neighbor in get_neighbors(cur_n_id):
                if is_red(neighbor) or is_blue(neighbor):
                    continue
                if is_red(cur_n_id): 
                    make_blue(neighbor)
                    blue += 1
                if is_blue(cur_n_id):
                    make_red(neighbor)
                    red += 1
                q.append(neighbor)
        
        return max(red,blue)
    
    for i in range(len(mat)):
        if is_red(i) or is_blue(i): continue
        res += bfs(i)
            
    return res

print(main(mat))




