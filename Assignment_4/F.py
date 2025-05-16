# import sys,io,os
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# print = sys.stdout.write

size = int(input())
x, y = list(map(int, input().split()))

res_moves = []

if x - 1 > 0:
    if y - 1 > 0: res_moves.append((x-1, y-1))     
    res_moves.append((x-1, y))
    if y + 1 <= size: res_moves.append((x-1, y + 1))

if y - 1 > 0: res_moves.append((x, y-1))

if y + 1 <= size: res_moves.append((x, y + 1))
    

if x + 1 <= size:
    if y - 1 > 0: res_moves.append((x+1, y-1))     
    res_moves.append((x+1, y))
    if y + 1 <= size: res_moves.append((x+1, y + 1))

res_str = ''
print(len(res_moves))
for move in res_moves:
    res_str += f"{move[0]} {move[1]}\n"

res_str = res_str[:-1]
print(res_str)