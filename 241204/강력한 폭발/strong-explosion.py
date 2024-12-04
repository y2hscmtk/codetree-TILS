'''
1이 적힌 위치에 폭탄 설치 가능
3가지 유형의 폭탄 설치 가능
가장 많은 영역을 초토화 시킬 수 있도록 프로그램 작성
'''
n = int(input())

graph = []
bomb_position = []

c = 0 # 폭탄 설치가 가능한 영역의 수
for i in range(n):
    row = list(map(int,input().split()))
    for j in range(n):
        if row[j] == 1: # 폭탄을 놓을 수 있는 위치라면 기록
            bomb_position.append((i,j))
            c+=1
    graph.append(row)

bomb_type = [] # 각 위치에 설치할 폭탄의 유형
# 어떤 폭탄을 설치할지 선정
def dfs(cnt):
    if cnt == n: # 10개 모두 설치 시
        count_distroied_position() # 폭파된 영역 카운트
        return
    
    # 1,2,3 3가지 유형 중 1개의 폭탄 설치
    for i in range(1,4):
        bomb_type.append(i)
        dfs(cnt+1)
        bomb_type.pop()

# 해당 자리에 폭탄을 둠으로서 몇개의 폭탄이 터졌을지 카운트
result = 0
# 폭탄 유형1, 2, 3
dx = [[],[-1,-2,1,2], [-1,1,0,0], [-1,-1,1,1]]
dy = [[],[0,0,0,0], [0,0,-1,1], [-1,1,-1,1]]
def count_distroied_position():
    global result
    visited = [[False]*n for _ in range(n)] # 각 영역에 폭탄이 터졌는지 안터졌는지 확인용
    
    count = 0 # 터진 영역의 개수
    for t in range(c): # c개의 폭탄 설치 예정
        type = bomb_type[t] # i위치에 설치된 폭탄의 유형
        x,y = bomb_position[t] # i번째 위치 초기 좌표
        if not visited[x][y]:
            visited[x][y] = True
            count += 1
        for i in range(len(dx[type])):
            nx,ny = x + dx[type][i], y + dy[type][i]
            # 영역을 벗어나지 않으면서 아직 터지지 않은 공간인 경우
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                count += 1
                visited[nx][ny] = True
    
    result = max(result,count) # 더 많이 터진 경우로 정답 갱신

dfs(0)
print(result)