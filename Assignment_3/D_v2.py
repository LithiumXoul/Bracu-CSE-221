a = 2
n = 5

def calc(a, n, m):
    l = 1 + a
    for _ in range(n-2):
        l *= a
        l += 1

    l *= a
    return l % m

# import time

# start = time.time()

# print(calc(12, 7000, 7))

# end = time.time()

# print(f'Time: {end - start}')


import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

res_arr = []
t = int(input())
for _ in range(t):
    a, n, m = list(map(int, input().split()))
    res_arr.append(str(calc(a,n,m)))

print("\n".join(res_arr))