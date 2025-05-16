inp_1 = input()
inp_2 = input()

arr_len, k = list(map(int, inp_1.split()))
arr = list(map(int,inp_2.split()))


for i in range(k- 1,-1, -1):
    print(arr[i], end = ' ')

print()