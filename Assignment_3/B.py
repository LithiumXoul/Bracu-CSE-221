def linear_max(arr):
    if len(arr) == 1:
        return arr[0]
    
    mid = len(arr) // 2
    l = linear_max(arr[:mid])
    r = linear_max(arr[mid:])

    if l > r: return l
    else: return r


def square_max(arr):
    if len(arr) == 1: return arr[0] ** 2

    mid = len(arr) // 2
    l = square_max(arr[:mid])
    r = square_max(arr[mid:])

    if l > r: return l
    else: return r


def sum_max(arr):
    if len(arr) == 1:
        return None
    
    mid = len(arr) // 2
    l_sum_max = sum_max(arr[:mid])
    r_sum_max = sum_max(arr[mid:])

    l_linear_max = linear_max(arr[:mid])
    r_square_max = square_max(arr[mid:])

    
    cross_max_sum = l_linear_max + r_square_max

    if l_sum_max == None: l_sum_max = float('-inf')
    if r_sum_max == None: r_sum_max = float('-inf')

    return max(cross_max_sum, l_sum_max, r_sum_max)

import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline


n = input()
arr = list(map(int, input().split()))

print(sum_max(arr))
