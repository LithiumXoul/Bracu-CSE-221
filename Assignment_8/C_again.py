class Set_Manager:
    def __init__(self, total_nodes):
        self.parent_l = [i for i in range(total_nodes + 1)]
        self.size = [1] * (total_nodes+1)

    def get_rep(self, i):
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

def sort_func(a):
    return a[2]

n, m = map(int, input().split())

edge_list = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edge_list.append((u, v, w))

# Sort edges by weight
edge_list.sort(key=sort_func)

# Find the best MST
def find_mst(exclude_edge_idx=-1):
    sets = Set_Manager(n)
    total_cost = 0
    mst_edges = []
    
    for i, edge in enumerate(edge_list):
        if i == exclude_edge_idx:
            continue
            
        u, v, w = edge
        
        if not sets.in_same_set(u, v):
            sets.union(u, v)
            total_cost += w
            mst_edges.append(i)
            
    # Check if we have a valid spanning tree (all nodes connected)
    # For a graph with n nodes, we need exactly n-1 edges in the MST
    if len(mst_edges) != n - 1:
        return float('inf'), []
        
    return total_cost, mst_edges

# Get the best MST
best_cost, best_mst_edge_indices = find_mst()

# If there's no valid MST
if len(best_mst_edge_indices) != n - 1:
    print(-1)
else:
    # Find the second-best MST
    second_best_cost = float('inf')
    
    # Try removing each edge from the best MST
    for edge_idx in best_mst_edge_indices:
        cost, _ = find_mst(edge_idx)
        
        # Update if this is better than our current second best but worse than the best
        if cost > best_cost and cost < second_best_cost:
            second_best_cost = cost
    
    # Output the result
    if second_best_cost == float('inf'):
        print(-1)
    else:
        print(second_best_cost)