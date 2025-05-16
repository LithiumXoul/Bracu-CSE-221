import sys,io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
print = sys.stdout.write


n = int(input())
adj_l = []
for i in range(n):
    adj_l.append([0] * n)

for k in range(n):
    adj_nodes = list(map(int, input().split()[1:]))
    for l in range(len(adj_nodes)):
        adj_l[k][adj_nodes[l]] = 1

res_str = ''
for z in range(len(adj_l)):
    res_str += ' '.join(list(map(str, adj_l[z])))
    res_str += '\n'

res_str = res_str[:-1]
print(res_str)