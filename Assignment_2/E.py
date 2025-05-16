import io,os,sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
print = sys.stdout.write


n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
res_arr = []

for _ in range(k):
    lb, hb = list(map(int, input().split()))
    lb_idx, hb_idx = None, None

    #looking for higher bound index

    l = 0
    r = len(arr) - 1

    while(l <= r):
        m = (l + r) // 2

        if arr[m] >= lb and (m == 0 or arr[m-1] < lb):
            lb_idx = m
            break

        elif arr[m] >= lb:
            r = m - 1
            continue

        elif arr[m] < lb:
            l = m + 1
            continue

    if lb_idx == None:
        res_arr.append(0)
        continue

    # looking for upper bound index

    l = 0
    r = len(arr) - 1

    while(l <= r):
        m = (l + r) // 2

        if arr[m] <= hb and (m == len(arr) - 1 or arr[m+1] > hb):
            hb_idx = m
            break

        elif arr[m] > hb:
            r = m - 1
            continue

        elif arr[m] <= hb:
            l = m + 1
            continue

    if hb_idx == None:
        res_arr.append(0)
        continue

    res_arr.append(hb_idx - lb_idx + 1)

print("\n".join(map(str, res_arr)))

