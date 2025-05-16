# import sys,io,os
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# print = sys.stdout.write



import math
n, q = list(map(int, input().split()))
adj_l = []
memo = {}
for i in range(1, n+1):
    adj_l.append([])
    for j in range(1, n+ 1):
        if i == j:
            continue
        
        if j == 1:
            adj_l[i - 1].append(1)

        elif (i,j) in memo or (j,i) in memo:
            adj_l[i - 1].append(j)
        elif math.gcd(i,j) == 1: 
            adj_l[i-1].append(j)
            memo[(i,j)] = 1

print(adj_l)

res_str = ''
for _ in range(q):
    x, k = list(map(int, input().split()))
    if len(adj_l[x-1]) < k:
        res_str += '-1\n'
    else:
        res_str += f'{adj_l[x-1][k-1]}\n'

res_str = res_str[:-1]
print(res_str)