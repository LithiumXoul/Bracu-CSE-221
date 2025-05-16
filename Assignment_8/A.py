n, k = list(map(int, input().split()))

parent_l = [i for i in range(n + 1)]
size = [1] * (n+1)
def get_rep(i):
    if parent_l[i] == i:
        return i
    
    parent_l[i] = get_rep(parent_l[i])
    return parent_l[i]

def union(a,b):
    if parent_l[a] == parent_l[b]:
        return
    
    rep_a = get_rep(a)
    rep_b = get_rep(b)

    if rep_a == rep_b:
        return size[rep_a]
    
    if size[rep_a] < size[rep_b]:
        rep_a, rep_b = rep_b, rep_a
    
    parent_l[rep_b] = rep_a
    size[rep_a] += size[rep_b]
    
    return size[rep_a]

res_arr = []
for _ in range(k):
    a, b = list(map(int, input().split()))
    union(a,b)
    new_rep = get_rep(a)  
    res_arr.append(str(size[new_rep]))


print('\n'.join(res_arr))
