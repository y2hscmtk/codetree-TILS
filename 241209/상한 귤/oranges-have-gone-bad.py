from collections import deque

# 상한 귤 넣어두기 
queue = deque()

n,k = map(int,input().split()) # 격자의 크기, 상한 귤의 개수
visited = [[-1]*n for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

data = []
for i in range(n):
    row = list(map(int,input().split()))
    for j in range(n):
        if row[j] == 2: # 상한귤 - 탐색 시작 좌표
            queue.append((i,j))
            visited[i][j] = 0 # 방문 처리
    data.append(row)

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1:
                # 조건 검사 - '귤이 있는 좌표로만 이동 가능 - 이미 상한 귤은 따로 검사 시작'
                if data[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))

bfs()

# 정답 출력
for row in visited:
    print(*row)
    