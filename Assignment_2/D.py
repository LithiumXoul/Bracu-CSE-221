import io,os,sys
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

t = int(input())
output = []


for _ in range(t):
    S = input()
    l = 0
    r = len(S) - 1
    res = -1

    while (l <= r):
        m = (l + r) // 2
        if  S[m] == '0': 
            l = m + 1
            continue

        elif S[m] == '1' and (m == 0 or S[m-1] == '0'):
            res = m
            break
        
        elif S[m] == '1':
            r = m - 1
            continue

    
    if res != -1:
        output.append(res + 1)
    else: output.append(res)

print("\n".join(map(str, output)))