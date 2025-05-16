class Set_Manager:
    def __init__(self, total_nodes):
        self.parent_l = [i for i in range(total_nodes + 1)]
        self.size = [1] * (total_nodes+1)

    def get_rep(self,i):
        if self.parent_l[i] == i:
            return i
        
        self.parent_l[i] = self.get_rep(self.parent_l[i])
        return self.parent_l[i]
    
    def union(self, a, b):
        if self.parent_l[a] == self.parent_l[b]:
            return
        
        rep_a = self.get_rep(a)
        rep_b = self.get_rep(b)

        if rep_a == rep_b:
            return self.size[rep_a]
        
        if self.size[rep_a] < self.size[rep_b]:
            rep_a, rep_b = rep_b, rep_a
        
        self.parent_l[rep_b] = rep_a
        self.size[rep_a] += self.size[rep_b]
        
        return self.size[rep_a]
    
    def in_same_set(self, a, b):
        res_a = self.get_rep(a)
        res_b = self.get_rep(b)

        if res_a == res_b: return True
        return False
    

n,m = list(map(int, input().split()))
set = Set_Manager(n)

edge_list = []
for _ in range(m):
    u, v, w = list(map(int, input().split()))
    edge_list.append((u,v,w))


def sort_func(a):
    return a[2]

edge_list.sort(key = sort_func)

sets = Set_Manager(n)

total_cost = 0

for edge in edge_list:
    u = edge[0]
    v = edge[1]
    if not sets.in_same_set(u,v):
        sets.union(u,v)
        total_cost += edge[2]

print(total_cost)
