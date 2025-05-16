
import sys,io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
print = sys.stdout.write

n, m = map(int, input().split())
    
u = list(map(int, input().split()))
v = list(map(int, input().split()))

deg_count = [0] * n
for i in range(m):
    deg_count[u[i] - 1] += 1
    deg_count[v[i] - 1] += 1

odd_deg_count = 0
for k in range(n):
    if deg_count[k] %2 == 1: odd_deg_count += 1

if odd_deg_count == 0 or odd_deg_count == 2:
    print('YES')
else:
    print('NO')