# import sys,io,os, time
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# print = sys.stdout.write

import time



import math
n, q = list(map(int, input().split()))

res_list = []
total_time = 0
for _ in range(q):
    x, k = list(map(int, input().split()))
    
    start = time.time()

    found = False
    cur_k = 1
    for i in range(1, n+1):
        if x == i:
            continue
        if cur_k == k and math.gcd(x,i) == 1:
            res_list.append(str(i))
            found = True
            break
        elif math.gcd(x,i) == 1:
            cur_k += 1
    
    if not found:
        res_list.append('-1')

    end = time.time()
    total_time += end-start

print('\n'.join(res_list))
print(total_time)