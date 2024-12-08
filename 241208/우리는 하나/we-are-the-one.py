from collections import deque
n,k,u,d = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]

city = []
for i in range(n):
    for j in range(n):
        city.append((i,j)) # 모든 도시 좌표 저장

# 두 도시의 높이차가 u이상 d인 경우만 이동 가능
dx = [0,0,-1,1]; dy = [-1,1,0,0]
visited = [[False]*n for _ in range(n)] # 방문 정보 확인 배
queue = deque() # 이동 시작할 k개의 도시
max_moveble_city = 0 # 이동 가능한 최대 도시 수

def visited_init():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False 

# k개 도시 선택
def dfs(s,cnt):
    if cnt == k:
        bfs()
        return
    
    for i in range(s,n*n):
        queue.append(city[i])
        dfs(i+1,cnt+1)
        if queue:
            queue.pop()

def bfs():
    global max_moveble_city
    visited_init()
    count = 0 # 현재 탐색에서 이동 가능한 도시의 수
    for x,y in queue:
        visited[x][y] = True
        count += 1
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                # 조건 검사 높이차가 u이상 d이하
                dist = abs(data[x][y] - data[nx][ny])
                if u<=dist<=d:
                    count += 1 # 지나갈수 있는 도시 추가
                    queue.append((nx,ny))
                    visited[nx][ny] = True
    
    # 이동 가능한 최대 도시 수 갱신
    max_moveble_city = max(max_moveble_city,count)

# 이동시작할 k개의 도시 선택
dfs(0,0)
print(max_moveble_city)
