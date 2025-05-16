import sys,io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
print = sys.stdout.write


n, m = list(map(int, input().split()))
adj_l = []
for i in range(n):
    adj_l.append([])

u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

for k in range(m):
    adj_l[u[k] - 1].append((v[k], w[k]))

res_str = ''
for l in range(n):
    res_str += f'{l + 1}: '
    for z in range(len(adj_l[l])):
        res_str += f'({adj_l[l][z][0]},{adj_l[l][z][1]}) '
    res_str = res_str[: - 1]
    res_str += '\n'
res_str = res_str[:-1]
print(res_str)