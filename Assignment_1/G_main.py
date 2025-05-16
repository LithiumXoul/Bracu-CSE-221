arr_len = int(input())
arr = []
for _ in range(arr_len):
    inp_arr = input().split()
    train_name = inp_arr[0]
    train_destination = inp_arr[4]
    train_time = inp_arr[6]

    arr.append([train_name, train_destination, train_time])


is_sorted = True
for i in range(arr_len - 1):
    for k in range(arr_len - 1 - i):
        train_name_1, train_time_1 = arr[k][0] , arr[k][2]
        train_name_2, train_time_2 = arr[k+1][0], arr[k+1][2]

        found = False
        smaller = True

        if len(train_name_1) <= len(train_name_2):
            for i in range(len(train_name_1)):
                if ord(train_name_1[i]) < ord(train_name_2[i]): 
                    smaller = True
                    found = True
                    break
                elif ord(train_name_1[i]) > ord(train_name_2[i]): 
                    smaller =  False
                    found = True
                    break
        else:
            for i in range(len(train_name_2)):
                if ord(train_name_1[i]) < ord(train_name_2[i]): 
                    smaller = True
                    found = True
                    break
                elif ord(train_name_1[i]) > ord(train_name_2[i]): 
                    smaller =  False
                    found = True
                    break

        if not found:
            if len(train_name_1) < len(train_name_2): 
                smaller = True
                found = True
            elif len(train_name_1) > len(train_name_2): 
                smaller = False
                found = True

        if not found:
            if int(train_time_1[:2]) > int(train_time_2[:2]): 
                smaller = True
                found = True
            elif int(train_time_1[:2]) < int(train_time_2[:2]): 
                smaller =  False
                found = True

        if not found:

            if int(train_time_1[3:]) > int(train_time_2[3:]): 
                smaller = True
            elif int(train_time_1[3:]) < int(train_time_2[3:]): 
                smaller =  False

        
        
        #
        if not smaller:
            is_sorted = False
            temp = arr[k]
            arr[k] = arr[k + 1]
            arr[k + 1] = temp
    if is_sorted:
        break

print()
for l in range(arr_len):
    print(f'{arr[l][0]} will departure for {arr[l][1]} at {arr[l][2]}')






