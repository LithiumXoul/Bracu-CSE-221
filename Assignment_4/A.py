import sys,io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

n, m = list(map(int, input().split()))
adj_m = []
for k in range(n):
    adj_m.append([0] * n)
for i in range(m):
    u, v, w = list(map(int, input().split()))
    adj_m[u - 1][v - 1] = w

res_str = ''
for i in range(n):
    res_str += ' '.join(list(map(str,adj_m[i])))
    res_str += '\n'
res_str = res_str[:-1]

sys.stdout.write(res_str)