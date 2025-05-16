n, m = list(map(int, input().split()))
mat = []
for i in range(n):
    mat.append([[]])
for _ in range(m):
    u, v = list(map(int, input().split()))
    mat[u - 1][0].append(v)

for node in mat:
    node.append(0)


import sys
sys.setrecursionlimit(2*100000+5)

def main(mat):
    
    output_list = []
    global contains_cycle
    contains_cycle = False

    def is_grey(src):
        if mat[src][1] == 1: return True
    def is_black(src):
        if mat[src][1] == 2: return True
    def make_grey(src):
        mat[src][1] = 1
    def make_black(src):
        mat[src][1] = 2

    def negative_one(num):
        return num - 1

    def get_neighbors(src):
        return list(map(negative_one, mat[src][0]))


    def dfs(src):
        global contains_cycle

        if is_grey(src):
            contains_cycle = True
            return

        if is_black(src):
            return
        
        make_grey(src)
        for neighbour in get_neighbors(src):
            dfs(neighbour)

        output_list.append(src + 1)
        make_black(src)

    for i in range(len(mat)):
        dfs(i)

    if contains_cycle:
        return ['-1']

    output_list.reverse()

    return list(map(str,output_list))

print(' '.join(main(mat)))