from collections import deque



def get_diamond(map, r, c):
    d=0
    def is_valid(r,c):
        if r < 0 or r >= len(map): return False
        if c < 0 or c >= len(map[0]): return False
        if map[r][c] == '#': return False
        if discovered_map[r][c] == 1: return False
        return True
    
    def get_children(r,c):
        res = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        return res

    q = deque()
    q.append((r,c))
    discovered_map[r][c] = 1

    while q:
        cur_r, cur_c = q.popleft()
        if map[cur_r][cur_c] == 'D': d += 1
        for child in get_children(cur_r,cur_c):
            child_r, child_c = child
            if is_valid(child_r, child_c):
                q.append((child_r, child_c))
                discovered_map[child_r][child_c] = 1
    
    return d

    


r, h = list(map(int, input().split()))
map = []
for i in range(r):
    row_str = input()
    row = []
    for char in row_str:
        row.append(char)
    map.append(row)

discovered_map = []
for _r in range(len(map)):
    _ = []
    for _c in range(len(map[0])):
        _.append(0)
    discovered_map.append(_)
    
max_diamonds = 0
for _r in range(r):
    for _c in range(h):
        if map[_r] [_c] == '#' or discovered_map[_r][ _c] == 1: continue
        cur_diamonds = get_diamond(map, _r, _c)
        if cur_diamonds > max_diamonds: max_diamonds = cur_diamonds


print(max_diamonds)
