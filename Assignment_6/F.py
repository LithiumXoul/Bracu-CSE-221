import heapq

def topological_sort(words):
    graph = [set() for _ in range(26)]  # Adjacency list for 26 letters
    in_degree = [0] * 26
    used = [False] * 26

    def add_edge(c1, c2):
        u = ord(c1) - ord('a')
        v = ord(c2) - ord('a')
        if v not in graph[u]:
            graph[u].add(v)
            in_degree[v] += 1

    # Mark used letters
    for word in words:
        for ch in word:
            used[ord(ch) - ord('a')] = True

    # Build graph from word pairs
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        mismatch_found = False
        for j in range(min_len):
            if w1[j] != w2[j]:
                add_edge(w1[j], w2[j])
                mismatch_found = True
                break
        if not mismatch_found and len(w1) > len(w2):
            return "-1"  # Invalid due to prefix rule

    # Topological sort using min-heap for lexicographically smallest result
    heap = []
    for i in range(26):
        if in_degree[i] == 0 and used[i]:
            heapq.heappush(heap, i)

    result = []
    while heap:
        u = heapq.heappop(heap)
        result.append(chr(u + ord('a')))
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heapq.heappush(heap, v)

    if len(result) != sum(used):
        return "-1"  # Not all used letters are in the result, must be a cycle

    return ''.join(result)

# Input
n = int(input())
words = [input().strip() for _ in range(n)]

# Output
print(topological_sort(words))
