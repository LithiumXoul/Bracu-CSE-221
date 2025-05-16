import sys,io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
print = sys.stdout.write

n , m = list(map(int, input().split()))

res_list = [0] * n

out = list(map(int, input().split()))
for i in range(m):
    res_list[out[i] - 1] -= 1
in_deg = list(map(int, input().split()))
for k in range(m):
    res_list[in_deg[k] - 1] += 1

print(' '.join(map(str, res_list)))
