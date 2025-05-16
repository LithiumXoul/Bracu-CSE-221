arr_len = int(input())
# arr_len = 8

def isSmaller(train_detail_1, train_detail_2): #does train 1 comes before train 2 ?
    tn1, td1, tt1 = train_detail_1
    tn2, td2, tt2 = train_detail_2

    z = 0
    while (z < len(tn1) and z < len(tn2)):
        if ord(tn1[z]) < ord(tn2[z]): return True
        elif ord(tn1[z]) > ord(tn2[z]): return False
        z += 1
    

    if len(tn1) < len(tn2): return True
    elif len(tn1) > len(tn2): return False

    if int(tt1[:2]) > int(tt2[:2]): return True
    elif int(tt1[:2]) < int(tt2[:2]): return False

    if int(tt1[3:]) > int(tt2[3:]): return True
    elif int(tt1[3:]) < int(tt2[3:]): return False

    return True

def isBigger(train_detail_1, train_detail_2):
    return not(isSmaller(train_detail_1, train_detail_2))


arr = []
for _ in range(arr_len):
    inp_arr = input().split()
    train_name = inp_arr[0]
    train_destination = inp_arr[4]
    train_time = inp_arr[6]

    arr.append([train_name, train_destination, train_time])

# input_arr = ['ABCD will departure for Mymensingh at 00:30',
# 'DhumketuExpress will departure for Chittagong at 02:30',
# 'ABC will departure for Dhaka at 17:30',
# 'ABCD will departure for Chittagong at 01:00',
# 'ABC will departure for Khulna at 03:00',
# 'ABC will departure for Barisal at 03:00',
# 'ABCE will departure for Sylhet at 23:05',
# 'PadmaExpress will departure for Dhaka at 19:30']

# arr = []
# for i in range(arr_len):
#     cur_tran = input_arr[i]
#     train_name = cur_tran.split()[0]
#     train_destination = cur_tran.split()[4]
#     train_time = cur_tran.split()[6]

#     arr.append([train_name, train_destination, train_time])

# print(arr)


is_sorted = True
for i in range(arr_len - 1):
    for k in range(arr_len - 1 - i):
        if isBigger(arr[k], arr[k+1]):
            is_sorted = False
            temp = arr[k]
            arr[k] = arr[k + 1]
            arr[k + 1] = temp
    if is_sorted:
        break

for _ in range(arr_len):
    print(arr[_])






