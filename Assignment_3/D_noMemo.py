def calc(a, n, m):

    q = 0
    for i in range(1, n + 1):
        q += mod_calc(a, i, m)


    return q % m

def mod_calc(a, b, m):
    if a == 1 or b == 0: return 1
    if b == 1:
        return a % m
    
    b1 = b // 2
    b2 = b-b1

    f1 = mod_calc(a,b1,m)
    f2 = mod_calc(a, b2, m)

    return (f1 * f2) % m
    




# import io,os
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

# res_arr = []
# t = int(input())
# for _ in range(t):
#     a, n, m = list(map(int, input().split()))
#     res_arr.append(str(calc(a,n,m)))

# print("\n".join(res_arr))

import time

start = time.time()

print(calc(12, 7000, 7))

end = time.time()

print(f'Time: {end - start}')