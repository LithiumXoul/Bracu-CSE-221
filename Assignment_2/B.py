import sys,io,os

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline


a_len = int(input())
a = list(map(int, input().split()))
b_len = int(input())
b = list(map(int, input().split()))


a_pnt = 0
b_pnt = 0

res = []

while (a_pnt < a_len and b_pnt < b_len):
    if a[a_pnt] < b[b_pnt]: 
        res.append(a[a_pnt])
        a_pnt += 1
    else:
        res.append(b[b_pnt])
        b_pnt += 1

while (a_pnt < a_len):
    res.append(a[a_pnt])
    a_pnt += 1

while (b_pnt < b_len):
    res.append(b[b_pnt])
    b_pnt += 1

sys.stdout.write(" ".join(map(str,res)))
