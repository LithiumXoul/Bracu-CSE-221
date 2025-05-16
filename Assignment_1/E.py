arr_len = int(input())
arr = list(map(int, input().split()))

is_sorted = True
for i in range(arr_len - 1):
    for k in range(arr_len - 1 - i):
        if arr[k] > arr[k + 1]:
            is_sorted = False
            temp = arr[k]
            arr[k] = arr[k + 1]
            arr[k + 1] = temp
    if is_sorted:
        break

for m in range(len(arr)):
    print(arr[m], end = ' ')
print()
