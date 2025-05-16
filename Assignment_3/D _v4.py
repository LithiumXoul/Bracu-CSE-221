def calc(a, n, m, memo = {}):

    if n == 1: 
        return a % m
    
    l = calc(a, n//2, m)
    if n//2 in memo:
        print('memo 1')
        r = ((memo[n//2]) * l) % m
    else:
        r = (mod_calc(a, n//2, m, memo) * l) % m
    if n%2 == 1:
        if n in memo:
            print('memo') 
            r += memo[n]
        else: r += mod_calc(a,n,m)
    res = (l + r) % m

    return res

def mod_calc(a, b, m, memo = {}):
    if a == 1 or b == 0: return 1
    if b == 1:
        return a % m
    
    b1 = b // 2
    b2 = b-b1

    f1 = None
    if b1 in memo:
        f1 = memo[b1]
    else:
        f1 = mod_calc(a,b1,m,memo)
        if not len(memo) > 40:
            memo[b1] = f1

    f2 = None
    if b2 in memo:
        f2 = memo[b2]
    else:
        f2 = mod_calc(a, b2, m, memo)
        if not len(memo) > 40:
            memo[b2] = f2

    return (f1 * f2) % m
    




import io,os
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

# res_arr = []
# t = int(input())
# for _ in range(t):
#     a, n, m = list(map(int, input().split()))
#     res_arr.append(str(calc(a,n,m)))

# print("\n".join(res_arr))

import time
start = time.time()

print(calc(2, 5, 9))

end = time.time()
print(end-start)