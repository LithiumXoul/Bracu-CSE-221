def meow(arr, output_arr = []):
    if len(arr) == 0: return output_arr
    if len(arr) == 1: 
        output_arr.append(arr[0])
        return output_arr

    mid = len(arr)//2
    output_arr.append(arr[mid])
    meow(arr[:mid],output_arr)
    meow(arr[mid+1:], output_arr)

    return output_arr


import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline


n = input()
arr = list(map(int,input().split()))

# arr = [1,2,3,4,5]

res = meow(arr)
print(" ".join(map(str,res)))
