import math, time
from functools import lru_cache

@lru_cache(maxsize=None)
def get_neighbors(x, n):
    """Returns sorted list of nodes connected to x (where gcd(x,j) = 1)"""
    neighbors = []
    for j in range(1, n + 1):
        if j != x and math.gcd(x, j) == 1:
            neighbors.append(j)
    return sorted(neighbors)

def main():
    total_time = 0
    n, q = map(int, input().split())
    
    
    results = []
    for _ in range(q):
        x, k = map(int, input().split())
        start = time.time()
        neighbors = get_neighbors(x, n)
        
        if k <= len(neighbors):
            results.append(str(neighbors[k - 1]))
        else:
            results.append("-1")
        end = time.time()
        total_time += end - start
    
    print("\n".join(results))
    print(total_time)

if __name__ == "__main__":
    main()