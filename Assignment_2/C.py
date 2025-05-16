import io,os

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline


n, k = list(map(int,input().split()))
arr = list(map(int,input().split()))


# n, k = 1, 1
# arr = [2,4,5,2,2]
# n = len(arr)


def max_len_subarray(n, k, arr):  

    l = 0
    r = 0

    cur_sum = arr[0]
    max_len = 0

    while (l < n-1):
        if l == r:
            if arr[l] <= k and max_len < 1: max_len = 1
            r += 1
            cur_sum += arr[r]
            continue

        cur_len = r-l+1

        if cur_sum <= k and cur_len > max_len:
            max_len = cur_len

        
        if cur_sum > k or r >= n-1:
            cur_sum -= arr[l]
            l += 1

        elif cur_sum <= k:
            r += 1
            cur_sum += arr[r]

    if arr[n-1] <= k and max_len < 1: max_len = 1

    print(max_len)

max_len_subarray(n,k,arr)