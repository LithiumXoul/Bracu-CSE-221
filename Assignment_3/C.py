import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

a, b = list(map(int, input().split()))
def calc(a, b, memo = {}):
    if b == 1:
        return a % 107
    
    b1 = b // 2
    b2 = b-b1

    f1 = None
    if b1 in memo:
        f1 = memo[b1]
    else:
        f1 = calc(a,b1)
        memo[b1] = f1

    f2 = None
    if b2 in memo:
        f2 = memo[b2]
    else:
        f2 = calc(a, b2)
        memo[b2] = f2

    return (f1 * f2) % 107



print(calc(a ,b))