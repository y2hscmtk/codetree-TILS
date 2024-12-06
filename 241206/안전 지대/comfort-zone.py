from collections import deque

result = 0 # 최대 안전영역의 수
result2 = 1 # 물에 최대로 잠기지 않게 하는 k의 값
dx = [0,0,-1,1]
dy = [-1,1,0,0]

n,m = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]

# 가장 큰 k의 값을 구하는 과정
max_k = 0
for row in data:
    max_k = max(max_k,max(row))

def bfs(s,e,k):
    global count
    queue = deque()
    queue.append((s,e))
    visited[s][e] = True # 방문 처리
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if data[nx][ny] > k: # 물에 잠기지 않은 지역이라면
                    visited[nx][ny] = True # 방문 처리
                    queue.append((nx,ny))
    count += 1 # 물에 잠기지 않는 영역의 수 증가

# 1부터 k까지에 대해서 
for k in range(1,max_k+1):
    visited = [[False]*m for _ in range(n)] # visited 배열 초기화
    # 각 배열의 탐색
    count = 0 # k일때 물에 잠기지 않는 영역의 수
    for i in range(n):
        for j in range(m):
            # 탐색 수행
            if data[i][j] > k and not visited[i][j]:
                bfs(i,j,k)
    if result < count:
        result = count
        result2 = k
print(result2,result)