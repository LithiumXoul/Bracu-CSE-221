def calc(a, n, m):

    if n == 1: 
        return a % m
    
    l = calc(a, n//2, m)
    r = (mod_calc(a, n//2, m) * l) % m
    if n%2 == 1:
        r += mod_calc(a,n,m)
    res = (l + r) % m

    return res

def mod_calc(a, b, m):
    return (a**b) % m    

import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

res_arr = []
t = int(input())
for _ in range(t):
    a, n, m = list(map(int, input().split()))
    res_arr.append(str(calc(a,n,m)))

print("\n".join(res_arr))


# print(calc(2, 5, 9))