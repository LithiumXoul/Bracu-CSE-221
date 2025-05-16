t = int(input())
for i in range(t):
    inp = input()

    _, first_num, op, last_num = inp.split()

    first_num = int(first_num)
    last_num = int(last_num)

    if op == '+':
        result = first_num + last_num
    elif op == '-':
        result = first_num - last_num
    elif op == '*':
        result = first_num * last_num
    elif op == '/':
        result = first_num / last_num
    
    print(result)