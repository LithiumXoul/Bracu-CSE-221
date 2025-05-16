from collections import deque

n = int(input())
x1, y1, x2, y2 = map(int, input().split())
x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1

if (x1, y1) == (x2, y2):
    print(0)
    exit()

directions = [(2, 1), (1, 2), (1, -2), (-1, 2),(-2, 1), (-2, -1), (-1, -2), (2, -1)]

def in_bounds(x, y):
    return 0 <= x < n and 0 <= y < n

visited_start = [[-1] * n for _ in range(n)]
visited_end = [[-1] * n for _ in range(n)]

q_start = deque()
q_end = deque()

q_start.append((x1, y1))
q_end.append((x2, y2))
visited_start[x1][y1] = 0
visited_end[x2][y2] = 0

while q_start and q_end:
    for _ in range(len(q_start)):
        x, y = q_start.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and visited_start[nx][ny] == -1:
                visited_start[nx][ny] = visited_start[x][y] + 1
                q_start.append((nx, ny))
                if visited_end[nx][ny] != -1:
                    print(visited_start[nx][ny] + visited_end[nx][ny])
                    exit()

    for _ in range(len(q_end)):
        x, y = q_end.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and visited_end[nx][ny] == -1:
                visited_end[nx][ny] = visited_end[x][y] + 1
                q_end.append((nx, ny))
                if visited_start[nx][ny] != -1:
                    print(visited_start[nx][ny] + visited_end[nx][ny])
                    exit()

print(-1)
