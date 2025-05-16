arr_len = int(input())
id_arr = list(map(int, input().split()))
marks_arr = list(map(int, input().split()))

# arr_len = 7
# id_arr = [7 ,4, 9, 3, 2, 5, 1]
# marks_arr = [40, 50, 50, 20, 10, 10, 10]


#selection sort

swap = 0
for i in range(arr_len - 1):
    cur_max_idx = None
    cur_max_val = None

    for k in range(i + 1, arr_len):
        if cur_max_val == None or marks_arr[k] > cur_max_val:
            cur_max_idx = k
            cur_max_val = marks_arr[k]

        elif marks_arr[k] == cur_max_val and id_arr[k] < id_arr[cur_max_idx]:
            cur_max_idx = k

    if marks_arr[cur_max_idx] > marks_arr[i]:
        swap += 1
        temp = marks_arr[i]
        marks_arr[i] = marks_arr[cur_max_idx]
        marks_arr[cur_max_idx] = temp

        temp = id_arr[i]
        id_arr[i] = id_arr[cur_max_idx]
        id_arr[cur_max_idx] = temp

    elif marks_arr[cur_max_idx] == marks_arr[i] and id_arr[cur_max_idx] < id_arr[i]:
        swap += 1
        temp = marks_arr[i]
        marks_arr[i] = marks_arr[cur_max_idx]
        marks_arr[cur_max_idx] = temp

        temp = id_arr[i]
        id_arr[i] = id_arr[cur_max_idx]
        id_arr[cur_max_idx] = temp

print(f'Minimum swaps: {swap}')
for m in range(arr_len):
    print(f"ID: {id_arr[m]} Mark: {marks_arr[m]}")
