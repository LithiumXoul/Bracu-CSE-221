def merge(a, b, inversion):
    # write your code here
    # a and b are two sorted list
    # merge function will return a sorted list after merging a and b
    i = 0
    j = 0
    res = []

    while (i < len(a) and j < len(b)):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            inversion[0] += len(a) - i
            res.append(b[j])
            j += 1
    while (i < len(a)):
        res.append(a[i])
        i += 1
    while (j < len(b)):
        res.append(b[j])
        j += 1

    return res

def mergeSort(arr, inversion = [0]):
    if len(arr) <= 1:
        return (arr,inversion[0])
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid], inversion)[0]  # write the parameter 
        a2 = mergeSort(arr[mid:], inversion)[0]  # write the parameter
        res = merge(a1, a2, inversion)
        return (res,inversion[0])       # complete the merge function above 
    


import io,os

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline


n = input()
arr = list(map(int, input().split()))
res_arr, inversion = mergeSort(arr)
res_arr_str = " ".join(map(str,res_arr))
print(inversion)
print(res_arr_str)
