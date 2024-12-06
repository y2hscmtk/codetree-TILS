from collections import deque
n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]

town_count = 0
people = []

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(s,e):
    queue = deque()
    queue.append((s,e))
    count = 1 # 마을 사람의 수
    visited[s][e] = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if data[nx][ny] == 1: # 인접한 사람이면
                    visited[nx][ny] = True # 방문 처리
                    queue.append((nx,ny))
                    count += 1 # 마을 사람 수 증가
    people.append(count)


for i in range(n):
    for j in range(n):
        if data[i][j] == 1 and not visited[i][j]:
            town_count += 1
            bfs(i,j)

print(town_count)

for p in sorted(people):
    print(p)