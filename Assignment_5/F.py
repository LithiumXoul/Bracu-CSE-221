import sys
sys.setrecursionlimit(2*1000000+5)




def copy_map(map):
    res_map = []
    for row in range(len(map)):
        cur_row = []
        for col in range(len(map[0])):
            cur_row.append(map[row][col])
        res_map.append(cur_row)
    return res_map


def get_diamond(map,r,c):
    if r < 0 or r >= len(map): return 0
    if c < 0 or c >= len(map[0]): return 0
    if map[r][c] == '#' or map[r][c] == 'v': return 0

    d = 0
    if map[r][c] == 'D': d += 1
    map[r][c] = 'v'
    d += get_diamond(map, r + 1, c)
    d += get_diamond(map, r - 1, c)
    d += get_diamond(map, r , c + 1)
    d += get_diamond(map, r , c - 1)

    return d


r, h = list(map(int, input().split()))
map = []
for i in range(r):
    row_str = input()
    row = []
    for char in row_str:
        row.append(char)
    map.append(row)
    
max_diamonds = 0
for _r in range(r):
    for _c in range(h):
        map_2 = copy_map(map)
        cur_diamonds = get_diamond(map_2, _r, _c)
        if cur_diamonds > max_diamonds: max_diamonds = cur_diamonds

print(max_diamonds)







